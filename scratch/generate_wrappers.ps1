$wrappers = @(
    "Invoke-GeneXusXpzExport.ps1",
    "Invoke-GeneXusXpzImport.ps1",
    "Open-GeneXusKbHeadless.ps1",
    "Test-GeneXusMsBuildSetup.ps1",
    "Test-GeneXusXpzImportPreview.ps1",
    "Build-KbIntelligenceIndex.ps1",
    "Query-KbIntelligenceIndex.ps1"
)

$targetDir = "d:\aaProyectos\Entorno04\.agents\skills\scripts"
if (-not (Test-Path $targetDir)) { New-Item -ItemType Directory -Path $targetDir }

foreach ($name in $wrappers) {
    $enginePath = "..\scripts-xpz\$name"
    $content = @"
# --- Wrapper: $name ---
# This is a wrapper for the engine script in scripts-xpz/
# Aligned with the methodology defined in README.md

`$scriptDir = Split-Path -Parent `$MyInvocation.MyCommand.Path
`$enginePath = Join-Path `$scriptDir "$enginePath"

if (-not (Test-Path `$enginePath)) {
    Write-Error "Engine script not found: `$enginePath"
    exit 1
}

& `$enginePath @PSBoundParameters
"@
    $content | Set-Content -Path (Join-Path $targetDir $name) -Encoding UTF8
}
