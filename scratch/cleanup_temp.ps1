# Script de limpieza segura para Windows 10
# Ejecutar con privilegios de administrador

Write-Host "Iniciando limpieza de archivos temporales..." -ForegroundColor Cyan

$tempFolders = @(
    "$env:TEMP\*",
    "C:\Windows\Temp\*",
    "C:\Windows\Prefetch\*",
    "C:\Windows\SoftwareDistribution\Download\*"
)

foreach ($folder in $tempFolders) {
    Write-Host "Limpiando: $folder"
    Remove-Item -Path $folder -Recurse -Force -ErrorAction SilentlyContinue
}

# Limpieza de Chrome Cache (si existe)
$chromeCache = "C:\Users\Sergio\AppData\Local\Google\Chrome\User Data\Default\Cache\*"
if (Test-Path $chromeCache) {
    Write-Host "Limpiando cache de Chrome..."
    Remove-Item -Path $chromeCache -Recurse -Force -ErrorAction SilentlyContinue
}

# Ejecutar Cleanmgr en modo silencioso (opcional, requiere intervención si no se pre-configura)
# Start-Process "cleanmgr.exe" -ArgumentList "/sagerun:1" -Wait

Write-Host "Limpieza completada." -ForegroundColor Green
