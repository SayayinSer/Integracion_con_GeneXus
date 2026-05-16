import os
import sys
import subprocess
import threading
import time
import socket
import psutil
import webbrowser
from fastapi import FastAPI, BackgroundTasks, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(title="GeneXus DevOps Panel")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# Global state
processes = {
    "backend": None,
    "frontend": None
}
logs = {
    "backend": [],
    "frontend": []
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.join(BASE_DIR, "Apis_Python_Notes", "backend")
FRONTEND_DIR = os.path.join(BASE_DIR, "Apis_Python_Notes", "frontend")

def is_port_in_use(port: int) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        return s.connect_ex(('127.0.0.1', port)) == 0

def kill_process_on_port(port: int):
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port:
                    proc.kill()
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

def stream_logs(process, name):
    for line in iter(process.stdout.readline, b''):
        if line:
            decoded_line = line.decode('utf-8', errors='replace').strip()
            logs[name].append(decoded_line)
            if len(logs[name]) > 200:
                logs[name].pop(0)

@app.get("/api/status")
def get_status():
    backend_running = processes["backend"] is not None and processes["backend"].poll() is None
    frontend_running = processes["frontend"] is not None and processes["frontend"].poll() is None
    
    return {
        "backend": {
            "running": backend_running,
            "port_in_use": is_port_in_use(8000)
        },
        "frontend": {
            "running": frontend_running,
            "port_in_use": is_port_in_use(3000)
        }
    }

@app.post("/api/backend/start")
def start_backend():
    if processes["backend"] and processes["backend"].poll() is None:
        return {"status": "already running"}
    
    if is_port_in_use(8000):
        kill_process_on_port(8000)
        time.sleep(1)
        
    logs["backend"] = ["Iniciando Backend FastAPI..."]
    env = os.environ.copy()
    
    processes["backend"] = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--reload", "--host", "127.0.0.1", "--port", "8000"],
        cwd=BACKEND_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=env
    )
    
    threading.Thread(target=stream_logs, args=(processes["backend"], "backend"), daemon=True).start()
    return {"status": "started"}

@app.post("/api/backend/stop")
def stop_backend():
    if processes["backend"]:
        processes["backend"].terminate()
        try:
            processes["backend"].wait(timeout=3)
        except:
            processes["backend"].kill()
        processes["backend"] = None
        logs["backend"].append("Backend detenido.")
    
    if is_port_in_use(8000):
        kill_process_on_port(8000)
    
    return {"status": "stopped"}

@app.post("/api/frontend/start")
def start_frontend():
    if processes["frontend"] and processes["frontend"].poll() is None:
        return {"status": "already running"}
    
    if is_port_in_use(3000):
        kill_process_on_port(3000)
        time.sleep(1)
        
    logs["frontend"] = ["Iniciando Frontend Next.js..."]
    
    # Use npm.cmd on Windows
    npm_cmd = "npm.cmd" if os.name == "nt" else "npm"
    
    processes["frontend"] = subprocess.Popen(
        [npm_cmd, "run", "dev"],
        cwd=FRONTEND_DIR,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT
    )
    
    threading.Thread(target=stream_logs, args=(processes["frontend"], "frontend"), daemon=True).start()
    return {"status": "started"}

@app.post("/api/frontend/stop")
def stop_frontend():
    if processes["frontend"]:
        # Terminate doesn't always kill npm child nodes on Windows easily, 
        # so we also kill the port explicitly
        processes["frontend"].terminate()
        processes["frontend"] = None
        logs["frontend"].append("Frontend detenido.")
        
    if is_port_in_use(3000):
        kill_process_on_port(3000)
        
    return {"status": "stopped"}

@app.get("/api/logs/{service}")
def get_logs(service: str):
    if service in logs:
        return {"logs": logs[service]}
    return {"logs": []}


HTML_CONTENT = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DevOps Panel - GeneXus</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        :root {
            --bg-dark: #0f172a;
            --bg-card: #1e293b;
            --primary: #0ea5e9;
            --success: #22c55e;
            --danger: #ef4444;
        }
        body {
            background-color: var(--bg-dark);
            color: #f8fafc;
            font-family: 'Inter', system-ui, sans-serif;
        }
        .glass {
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }
        .log-container {
            background: #020617;
            border-radius: 0.5rem;
            padding: 1rem;
            font-family: 'Courier New', monospace;
            font-size: 0.85rem;
            height: 300px;
            overflow-y: auto;
            color: #94a3b8;
        }
        .scrollbar-hide::-webkit-scrollbar {
            display: none;
        }
    </style>
</head>
<body class="p-8">

    <div class="max-w-6xl mx-auto">
        <header class="flex justify-between items-center mb-8">
            <div>
                <h1 class="text-3xl font-bold text-[#0ea5e9] flex items-center gap-3">
                    <i data-lucide="server-cog"></i> DevOps Control Panel
                </h1>
                <p class="text-slate-400 mt-2">Gestión y orquestación del entorno local.</p>
            </div>
            <div class="flex gap-4">
                <button onclick="startAll()" class="bg-[#0ea5e9] hover:bg-[#38bdf8] text-white px-6 py-2 rounded-lg font-semibold transition-all shadow-[0_0_15px_rgba(14,165,233,0.3)] flex items-center gap-2">
                    <i data-lucide="play-circle"></i> Iniciar Todo
                </button>
                <button onclick="stopAll()" class="bg-slate-700 hover:bg-[#ef4444] text-white px-6 py-2 rounded-lg font-semibold transition-all flex items-center gap-2">
                    <i data-lucide="stop-circle"></i> Detener Todo
                </button>
            </div>
        </header>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
            
            <!-- BACKEND CARD -->
            <div class="glass rounded-xl p-6 flex flex-col gap-4 shadow-xl">
                <div class="flex justify-between items-center border-b border-slate-700 pb-4">
                    <div class="flex items-center gap-3">
                        <i data-lucide="database" class="text-[#0ea5e9]"></i>
                        <h2 class="text-xl font-bold">Backend (FastAPI)</h2>
                    </div>
                    <div id="backend-status" class="px-3 py-1 rounded-full text-xs font-bold bg-slate-800 text-slate-400 border border-slate-600 flex items-center gap-2">
                        <div class="w-2 h-2 rounded-full bg-slate-400"></div> APAGADO
                    </div>
                </div>

                <div class="flex gap-3">
                    <button id="btn-start-backend" onclick="toggleService('backend', 'start')" class="flex-1 bg-slate-800 hover:bg-[#22c55e] border border-slate-600 hover:border-[#22c55e] transition-colors py-2 rounded-lg flex items-center justify-center gap-2">
                        <i data-lucide="power"></i> Iniciar
                    </button>
                    <button onclick="toggleService('backend', 'stop')" class="flex-1 bg-slate-800 hover:bg-[#ef4444] border border-slate-600 hover:border-[#ef4444] transition-colors py-2 rounded-lg flex items-center justify-center gap-2">
                        <i data-lucide="square"></i> Detener
                    </button>
                </div>

                <div class="log-container scrollbar-hide mt-2" id="backend-logs">
                    Esperando inicialización...
                </div>
            </div>

            <!-- FRONTEND CARD -->
            <div class="glass rounded-xl p-6 flex flex-col gap-4 shadow-xl">
                <div class="flex justify-between items-center border-b border-slate-700 pb-4">
                    <div class="flex items-center gap-3">
                        <i data-lucide="layout-template" class="text-[#0ea5e9]"></i>
                        <h2 class="text-xl font-bold">Frontend (Next.js)</h2>
                    </div>
                    <div id="frontend-status" class="px-3 py-1 rounded-full text-xs font-bold bg-slate-800 text-slate-400 border border-slate-600 flex items-center gap-2">
                        <div class="w-2 h-2 rounded-full bg-slate-400"></div> APAGADO
                    </div>
                </div>

                <div class="flex gap-3">
                    <button id="btn-start-frontend" onclick="toggleService('frontend', 'start')" class="flex-1 bg-slate-800 hover:bg-[#22c55e] border border-slate-600 hover:border-[#22c55e] transition-colors py-2 rounded-lg flex items-center justify-center gap-2">
                        <i data-lucide="power"></i> Iniciar
                    </button>
                    <button onclick="toggleService('frontend', 'stop')" class="flex-1 bg-slate-800 hover:bg-[#ef4444] border border-slate-600 hover:border-[#ef4444] transition-colors py-2 rounded-lg flex items-center justify-center gap-2">
                        <i data-lucide="square"></i> Detener
                    </button>
                </div>

                <div class="log-container scrollbar-hide mt-2" id="frontend-logs">
                    Esperando inicialización...
                </div>
            </div>

        </div>
    </div>

    <script>
        lucide.createIcons();

        async function toggleService(service, action) {
            await fetch(`/api/${service}/${action}`, { method: 'POST' });
            updateStatus();
        }

        async function startAll() {
            await toggleService('backend', 'start');
            setTimeout(() => toggleService('frontend', 'start'), 2000);
        }

        async function stopAll() {
            await toggleService('frontend', 'stop');
            await toggleService('backend', 'stop');
        }

        async function updateStatus() {
            try {
                const res = await fetch('/api/status');
                const data = await res.json();
                
                const updateBadge = (id, running, inUse) => {
                    const el = document.getElementById(id);
                    if (running) {
                        el.className = "px-3 py-1 rounded-full text-xs font-bold bg-green-900/30 text-green-400 border border-green-700 flex items-center gap-2";
                        el.innerHTML = '<div class="w-2 h-2 rounded-full bg-green-400 animate-pulse"></div> CORRIENDO';
                    } else if (inUse) {
                        el.className = "px-3 py-1 rounded-full text-xs font-bold bg-orange-900/30 text-orange-400 border border-orange-700 flex items-center gap-2 cursor-help";
                        el.innerHTML = '<div class="w-2 h-2 rounded-full bg-orange-400"></div> PUERTO BLOQUEADO (Click Start para limpiar)';
                    } else {
                        el.className = "px-3 py-1 rounded-full text-xs font-bold bg-slate-800 text-slate-400 border border-slate-600 flex items-center gap-2";
                        el.innerHTML = '<div class="w-2 h-2 rounded-full bg-slate-400"></div> APAGADO';
                    }
                };

                updateBadge('backend-status', data.backend.running, data.backend.port_in_use);
                updateBadge('frontend-status', data.frontend.running, data.frontend.port_in_use);
            } catch (e) {
                console.error("Panel desconectado", e);
            }
        }

        async function updateLogs() {
            for (const svc of ['backend', 'frontend']) {
                try {
                    const res = await fetch(`/api/logs/${svc}`);
                    const data = await res.json();
                    const el = document.getElementById(`${svc}-logs`);
                    if (data.logs.length > 0) {
                        const isScrolledToBottom = el.scrollHeight - el.clientHeight <= el.scrollTop + 1;
                        el.innerHTML = data.logs.join('<br>');
                        if (isScrolledToBottom) {
                            el.scrollTop = el.scrollHeight;
                        }
                    }
                } catch (e) {}
            }
        }

        // Loops
        setInterval(updateStatus, 2000);
        setInterval(updateLogs, 1000);
        updateStatus();
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def index():
    return HTML_CONTENT

if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("http://localhost:9999")
    
    threading.Thread(target=open_browser, daemon=True).start()
    uvicorn.run(app, host="127.0.0.1", port=9999, log_level="error")
