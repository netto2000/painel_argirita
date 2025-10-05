# Orquestrador para execução sequencial no PowerShell PainelArgirita

$env:PYTHONPATH = (Get-Location)

Write-Host "Executando coleta de dados Prefeitura..."
python -m scripts.coleta.coleta_prefeitura_api
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na coleta Prefeitura"; exit $LASTEXITCODE }

Write-Host "Executando coleta de dados Câmara..."
python -m scripts.coleta.coleta_camara_api_real
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na coleta Câmara"; exit $LASTEXITCODE }

Write-Host "Executando coleta de dados SICONFI..."
python -m scripts.coleta.coleta_siconfi
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na coleta SICONFI"; exit $LASTEXITCODE }

Write-Host "Executando coleta de dados TCE..."
python -m scripts.coleta.coleta_tce
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na coleta TCE"; exit $LASTEXITCODE }

Write-Host "Processando dados Câmara..."
python -m scripts.processamento.processar_camara
if ($LASTEXITCODE -ne 0) { Write-Error "Erro no processamento Câmara"; exit $LASTEXITCODE }

Write-Host "Processando dados Prefeitura..."
python -m scripts.processamento.processar_prefeitura
if ($LASTEXITCODE -ne 0) { Write-Error "Erro no processamento Prefeitura"; exit $LASTEXITCODE }

Write-Host "Processando dados TCE..."
python -m scripts.processamento.processar_tce
if ($LASTEXITCODE -ne 0) { Write-Error "Erro no processamento TCE"; exit $LASTEXITCODE }

Write-Host "Comparando fontes de dados..."
python -m scripts.comparacao.comparar_fontes
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na comparação"; exit $LASTEXITCODE }

Write-Host "Verificando integridade..."
python -m scripts.verificacao.verificar_integridade
if ($LASTEXITCODE -ne 0) { Write-Error "Erro na verificação"; exit $LASTEXITCODE }

Write-Host "Abrindo dashboard visual (Streamlit)..."
start streamlit run scripts.visualizacao.dashboard_main.py

Write-Host "Execução finalizada com sucesso!"
