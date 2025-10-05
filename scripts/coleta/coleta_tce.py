"""
Nome: coleta_tce.py
Finalidade: Baixar páginas HTML do Painel Suricato (TCE)
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import requests
from scripts.config import DIR_TCE_PORTAL, TIMEOUT_REQUESTS
from scripts.utilitarios.salvar_html import salvar_html
from scripts.utilitarios.logs import log_ok, log_warn, log_info

URLS = {
    "desp_pessoal": "https://www.tce.mg.gov.br/PainelSuricato/Detalhe/1HMP1VP1Y4",
    "empenho": "https://www.tce.mg.gov.br/PainelSuricato/Detalhe/1HMP1VP1Y4",
    "orgao": "https://www.tce.mg.gov.br/PainelSuricato/Detalhe/1HMP1VP1Y4"
}

def main():
    log_info("🚀 Iniciando coleta_tce")
    os.makedirs(DIR_TCE_PORTAL, exist_ok=True)
    for nome, url in URLS.items():
        try:
            resposta = requests.get(url, timeout=TIMEOUT_REQUESTS)
            resposta.raise_for_status()
            out_path = os.path.join(DIR_TCE_PORTAL, f"{nome}.html")
            salvar_html(out_path, resposta.text)
        except Exception as e:
            log_warn(f"Erro ao baixar {nome}: {e}")
    log_ok("✅ Coleta TCE finalizada")

if __name__ == "__main__":
    main()
