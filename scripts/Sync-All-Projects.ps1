# Script Maestro de Nivelacion y Respaldo Multi-Proyecto para GeneXus Skills y MCP
# Autor: Antigravity Orchestrator
# Fecha: 2026-05-21

$ErrorActionPreference = "Stop"
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"

$globalSkills = "$env:USERPROFILE\.gemini\config\skills"
$globalMcpConfig = "$env:USERPROFILE\.gemini\config\mcp_config.json"

$projects = @(
    @{
        Name = "Entorno04"
        LocalSkills = "D:\aaProyectos\Entorno04\.agents\skills"
        ConfigFolder = "D:\aaProyectos\Entorno04"
        BackupDir = "D:\aaProyectos\Entorno04\Backups"
    },
    @{
        Name = "Entorno01"
        LocalSkills = "D:\aaProyectos\Entorno01\.agents\skills"
        ConfigFolder = "D:\aaProyectos\Entorno01\.agents"
        BackupDir = "D:\aaProyectos\Entorno01\Backups"
    },
    @{
        Name = "Entorno02"
        LocalSkills = "D:\aaProyectos\Entorno02\.agents\skills"
        ConfigFolder = "D:\aaProyectos\Entorno02\.agents"
        BackupDir = "D:\aaProyectos\Entorno02\Backups"
    },
    @{
        Name = "Entorno03"
        LocalSkills = "D:\aaProyectos\Entorno03\AlisoWeb\.agents\skills"
        ConfigFolder = "D:\aaProyectos\Entorno03\AlisoWeb\.agents"
        BackupDir = "D:\aaProyectos\Entorno03\AlisoWeb\Backups"
    }
)

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host " INICIANDO PROCESO MAESTRO DE NIVELACION Y RESPALDO MULTI-PROYECTO" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

foreach ($proj in $projects) {
    Write-Host ""
    Write-Host ">>> Procesando proyecto: $($proj.Name) <<<" -ForegroundColor Green
    
    $localSkills = $proj.LocalSkills
    $configFolder = $proj.ConfigFolder
    $backupRoot = Join-Path $proj.BackupDir "Skills_Backup_$timestamp"
    
    # 1. Validaciones
    if (-not (Test-Path $localSkills)) {
        Write-Host "[-] ADVERTENCIA: La ruta de Skills locales no existe para $($proj.Name): $localSkills" -ForegroundColor Yellow
        Write-Host "    Se omitira este proyecto." -ForegroundColor Yellow
        continue
    }
    
    # 2. Crear carpeta de Backup
    Write-Host "[+] Creando directorio de respaldo en: $backupRoot" -ForegroundColor Gray
    New-Item -ItemType Directory -Path $backupRoot -Force | Out-Null
    
    # 3. Copia de Seguridad Local y Global de Skills (Excluyendo carpetas pesadas/sistemicas)
    Write-Host "[+] Respaldando Skills Locales..." -ForegroundColor Gray
    robocopy $localSkills (Join-Path $backupRoot "Local") /E /XD .git .context node_modules /XF .git* /NFL /NDL /NJH /NJS /R:0 /W:0 | Out-Null
    
    Write-Host "[+] Respaldando Skills Globales..." -ForegroundColor Gray
    if (Test-Path $globalSkills) {
        robocopy $globalSkills (Join-Path $backupRoot "Global") /E /XD .git .context node_modules /XF .git* /NFL /NDL /NJH /NJS /R:0 /W:0 | Out-Null
    } else {
        Write-Host "[-] Skills Globales no encontradas en $globalSkills" -ForegroundColor Yellow
    }
    
    # 4. Respaldo de Archivos de Configuracion del Proyecto (*config.json)
    Write-Host "[+] Respaldando archivos de configuracion del proyecto..." -ForegroundColor Gray
    if (Test-Path $configFolder) {
        Get-ChildItem -Path $configFolder -Filter "*config.json" | ForEach-Object {
            Copy-Item $_.FullName (Join-Path $backupRoot $_.Name) -Force
            Write-Host "    Archivo respaldado: $($_.Name)" -ForegroundColor DarkGray
        }
    }
    
    # 5. Respaldo del MCP Config Global
    if (Test-Path $globalMcpConfig) {
        Copy-Item $globalMcpConfig (Join-Path $backupRoot "global_mcp_config.json") -Force
        Write-Host "    Archivo global MCP respaldado: global_mcp_config.json" -ForegroundColor DarkGray
    }
    
    # 6. Nivelacion: Local -> Global (Copiar nuevas y actualizadas)
    Write-Host "[+] Nivelando Local -> Global..." -ForegroundColor Yellow
    robocopy $localSkills $globalSkills /E /XO /XD .git .context node_modules /XF .git* /NFL /NDL /NJH /NJS /R:0 /W:0 | Out-Null
    
    # 7. Nivelacion: Global -> Local (Copiar nuevas y actualizadas)
    Write-Host "[+] Nivelando Global -> Local..." -ForegroundColor Yellow
    robocopy $globalSkills $localSkills /E /XO /XD .git .context node_modules /XF .git* /NFL /NDL /NJH /NJS /R:0 /W:0 | Out-Null
    
    Write-Host "[+] Nivelacion y respaldos completados para $($proj.Name)." -ForegroundColor Green
    Write-Host "[+] Backup en: $backupRoot" -ForegroundColor DarkCyan
}

Write-Host ""
Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host " PROCESO MULTI-PROYECTO TERMINADO CON EXITO" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan
