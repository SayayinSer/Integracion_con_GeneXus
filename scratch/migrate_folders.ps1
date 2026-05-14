# Script de migración de carpetas con Uniones de Directorio (Junctions)
# Ejecutar como Administrador

function Move-FolderWithJunction {
    param (
        [string]$Source,
        [string]$Destination
    )

    if (-not (Test-Path $Source)) {
        Write-Warning "No se encontró el origen: $Source"
        return
    }

    if (Test-Path $Destination) {
        Write-Warning "El destino ya existe: $Destination. Saltando..."
        return
    }

    Write-Host "Migrando de $Source a $Destination..." -ForegroundColor Cyan

    # Crear carpeta de destino si no existe
    New-Item -ItemType Directory -Path (Split-Path $Destination -Parent) -Force | Out-Null

    # Mover usando Robocopy (robusto para permisos)
    # /E: Subdirectorios (incluyendo vacíos)
    # /MOVE: Borra de origen después de copiar
    # /XJ: Excluye puntos de unión (evita recursión infinita)
    robocopy "$Source" "$Destination" /E /MOVE /XJ /R:3 /W:5

    if ($LASTEXITCODE -lt 8) {
        Write-Host "Copiado exitoso. Creando unión..." -ForegroundColor Yellow
        cmd /c "mklink /J `"$Source`" `"$Destination`""
        Write-Host "Unión creada con éxito." -ForegroundColor Green
    } else {
        Write-Error "Error en robocopy al mover $Source"
    }
}

# Definir carpetas a mover
$baseDest = "D:\MigratedPrograms"

Move-FolderWithJunction -Source "C:\Users\Sergio\AppData\Local\Spotify" -Destination "$baseDest\Spotify"
Move-FolderWithJunction -Source "C:\Users\Sergio\AppData\Local\Google" -Destination "$baseDest\Google"
Move-FolderWithJunction -Source "C:\Program Files (x86)\GeneXus" -Destination "$baseDest\GeneXus_x86"
Move-FolderWithJunction -Source "C:\Program Files\Apache Software Foundation" -Destination "$baseDest\Apache"

Write-Host "Proceso de migración finalizado." -ForegroundColor Green
