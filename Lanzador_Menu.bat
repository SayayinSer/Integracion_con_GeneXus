@echo off
title DevOps Launcher Panel
echo Iniciando DevOps Launcher (FastAPI)...
echo Por favor espere mientras se carga el panel...

:: Check if psutil is installed
python -c "import psutil" >nul 2>&1
if %errorlevel% neq 0 (
    echo Instalando dependencias del panel...
    pip install fastapi uvicorn psutil
)

:: Start the python script in the background
start /B python DevOps_Launcher.py

echo.
echo Panel iniciado en segundo plano. 
echo Se abrira automaticamente su navegador en unos segundos.
echo (Cierre esta ventana cuando lo desee, el panel seguira ejecutandose en el navegador)
powershell -command "Start-Sleep -Seconds 5"
exit
