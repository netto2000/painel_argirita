# ============================================================
# 🚀 Abrir PowerShell 7 com ambiente virtual ativo
# Projeto: Painel_Argirita
# ============================================================

Write-Host "🚀 Abrindo PowerShell 7 com ambiente virtual ativo..." -ForegroundColor Cyan
Set-Location "C:\Users\nando\Documents\Painel_Argirita"
& "C:\Users\nando\Documents\Painel_Argirita\venv\Scripts\Activate.ps1"
Write-Host "✅ Ambiente virtual ativo em: $(Get-Location)" -ForegroundColor Green
