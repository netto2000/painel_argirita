@echo off
chcp 65001 >nul
cd /d "%~dp0"

where pwsh >nul 2>nul
if %errorlevel%==0 (
    echo Abrindo PowerShell 7...
    start "" pwsh -NoExit -Command "Set-Location -LiteralPath '%CD%'; .\venv\Scripts\Activate.ps1"
) else (
    echo PowerShell 7 nao encontrado. Abrindo PowerShell padrao...
    start "" powershell -NoExit -Command "Set-Location -LiteralPath '%CD%'; .\venv\Scripts\activate"
)
