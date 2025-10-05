function Show-EstruturaProjeto {
    $raiz = Get-Location
    Write-Host "`n🌳 ESTRUTURA DO PROJETO: $($raiz.Path)`n" -ForegroundColor Cyan
    
    # Mostrar estrutura principal
    Get-ChildItem -Directory | ForEach-Object {
        Write-Host "📁 $($_.Name)" -ForegroundColor Green
        Get-ChildItem -Path $_.FullName -Directory -ErrorAction SilentlyContinue | ForEach-Object {
            Write-Host "   ├── 📁 $($_.Name)" -ForegroundColor Yellow
            Get-ChildItem -Path $_.FullName -Directory -ErrorAction SilentlyContinue | ForEach-Object {
                Write-Host "   │   └── 📁 $($_.Name)" -ForegroundColor Blue
            }
        }
    }
    
    # Mostrar arquivos principais na raiz
    Write-Host "`n📄 ARQUIVOS PRINCIPAIS:" -ForegroundColor Cyan
    Get-ChildItem -File | Where-Object { 
        $_.Name -match "\.(py|ps1|md|txt|json)$" -and $_.Name -notmatch "^_" 
    } | ForEach-Object {
        Write-Host "   📄 $($_.Name)" -ForegroundColor White
    }
}

Show-EstruturaProjeto