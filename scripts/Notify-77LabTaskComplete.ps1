#requires -version 5.1
<#
.SYNOPSIS
Wrapper local para notificacao de conclusao de tarefa.

.DESCRIPTION
Emite um sinal visual/sonoro ou registra em log a conclusao de uma operacao
longa na pasta paralela da KB.
#>

param(
    [string]$Message = "Tarefa concluida com sucesso."
)

Write-Host ""
Write-Host "--------------------------------------------------" -ForegroundColor Cyan
Write-Host $Message -ForegroundColor Green
Write-Host "--------------------------------------------------" -ForegroundColor Cyan
[console]::Beep(440, 500)
