import os
from pathlib import Path

DIR_BASE = Path(__file__).resolve().parent.parent

ENCODING = "utf-8"

DIR_DADOS = DIR_BASE / "dados"
DIR_BRUTOS = DIR_DADOS / "brutos"
DIR_PROCESSADOS = DIR_DADOS / "processados"
DIR_LOGS = DIR_BASE / "logs"

DIR_CAMARA_API = DIR_BRUTOS / "camara"
DIR_PREFEITURA_API = DIR_BRUTOS / "prefeitura"
DIR_SICONFI_API = DIR_BRUTOS / "siconfi"
DIR_TCE_API = DIR_BRUTOS / "tce"
# Alias utilizado por coletores que salvam HTML do portal do TCE
# Mantemos compatibilidade com scripts que importam `DIR_TCE_PORTAL`
DIR_TCE_PORTAL = DIR_TCE_API

DIR_CAMARA_PROC = DIR_PROCESSADOS / "camara"
DIR_PREFEITURA_PROC = DIR_PROCESSADOS / "prefeitura"
DIR_SICONFI_PROC = DIR_PROCESSADOS / "siconfi"
DIR_TCE_PROC = DIR_PROCESSADOS / "tce"

URL_DADOS_ABERTOS_CAMARA = "https://cm-argirita.publicacao.siplanweb.com.br"
URL_DADOS_ABERTOS_PREF = "https://argirita.mg.gov.br/api"
URL_DADOS_ABERTOS_SICONFI = "https://siconfi.tesouro.gov.br/api"
URL_DADOS_ABERTOS_TCE = "https://www.tce.mg.gov.br/PainelSuricato"

TIMEOUT_REQUESTS = 30

ANOS = [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]

CATEGORIAS = ["camara", "prefeitura", "siconfi", "tce"]

for path in [
    DIR_DADOS, DIR_BRUTOS, DIR_PROCESSADOS, DIR_LOGS,
    DIR_CAMARA_API, DIR_PREFEITURA_API, DIR_SICONFI_API, DIR_TCE_API,
    DIR_CAMARA_PROC, DIR_PREFEITURA_PROC, DIR_SICONFI_PROC, DIR_TCE_PROC,
]:
    os.makedirs(path, exist_ok=True)
