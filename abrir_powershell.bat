@echo off
chcp 65001 > nul
cd /d %~dp0

REM Tenta abrir PowerShell 7, se disponível
where pwsh > nul 2>&1
if %errorlevel% == 0 (
    echo Abrindo PowerShell 7 com ambiente virtual ativado...
    start pwsh -NoExit -Command "& {Set-Location -LiteralPath '%cd%'; .\venv\Scripts\Activate.ps1}"
) else (
    echo PowerShell 7 nao encontrado. Abrindo PowerShell padrão...
    start powershell -NoExit -Command "& {Set-Location -LiteralPath '%cd%'; .\venv\Scripts\Activate.ps1}"
)
