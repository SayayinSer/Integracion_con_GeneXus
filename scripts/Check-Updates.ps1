$skillsPath = "D:\aaProyectos\Entorno04\.agents\skills"
$mcpPath = "D:\aaProyectos\Entorno04\Genexus18MCP"

function Check-Repo($path, $name) {
    if (-not (Test-Path $path)) { return $false }
    Push-Location $path
    git fetch origin
    $status = git status -uno
    $behind = ($status -match "Your branch is behind")
    Pop-Location
    return $behind
}

$skillsUpdates = Check-Repo $skillsPath "Skills"
$mcpUpdates = Check-Repo $mcpPath "GeneXus18MCP"

if ($skillsUpdates -or $mcpUpdates) {
    $msg = "Hay actualizaciones disponibles en tus repositorios de Antigravity:`n"
    if ($skillsUpdates) { $msg += "- GeneXus-XPZ-Skills`n" }
    if ($mcpUpdates) { $msg += "- GeneXus18MCP`n" }
    $msg += "`nPor favor, pide a Antigravity que realice la nivelación (Nivelar / Actualizar)."
    
    Add-Type -AssemblyName PresentationCore,PresentationFramework
    [System.Windows.MessageBox]::Show($msg, "Actualizaciones de Entorno04", "OK", "Information")
}
