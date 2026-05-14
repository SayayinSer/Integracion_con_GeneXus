#requires -version 5.1
<#
.SYNOPSIS
Wrapper local para gate de colisao de pacote da pasta paralela (77Lab).

.DESCRIPTION
Executa o script compartilhado `Test-XpzPackageCollision.ps1` antes de qualquer
gravacao de `NomeCurto_GUID_YYYYMMDD_nn.import_file.xml` em
`PacotesGeradosParaImportacaoNaKbNoGenexus`.

.PARAMETER FrontPrefix
Prefixo nominal da frente no formato `NomeCurto_GUID_YYYYMMDD`.

.PARAMETER NN
Rodada curta pretendida para o pacote, por exemplo `01`.

.PARAMETER OutputDir
Caminho opcional da pasta de saida.

.PARAMETER SharedSkillsRoot
Raiz local da base compartilhada `GeneXus-XPZ-Skills`.
#>

param(
    [Parameter(Mandatory = $true)]
    [string]$FrontPrefix,

    [Parameter(Mandatory = $true)]
    [string]$NN,

    [string]$OutputDir,

    [string]$SharedSkillsRoot = "d:\aaProyectos\Entorno04\.agents\skills"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

if (-not $OutputDir) {
    $repoRoot = Split-Path -Parent $PSScriptRoot
    $OutputDir = Join-Path $repoRoot "PacotesGeradosParaImportacaoNaKbNoGenexus"
}

$enginePath = Join-Path $SharedSkillsRoot "scripts\Test-XpzPackageCollision.ps1"
if (-not (Test-Path -LiteralPath $enginePath)) {
    throw "Shared package collision script not found: $enginePath"
}

& $enginePath -FrontPrefix $FrontPrefix -NN $NN -OutputDir $OutputDir
