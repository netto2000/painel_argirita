"""
Nome: coleta_prefeitura_api.py
Finalidade: Baixar dados da API da Prefeitura
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
from scripts.config import DIR_PREFEITURA_API, ANOS, URL_DADOS_ABERTOS_PREF
from scripts.utilitarios.fetch_json_endpoint import fetch_and_save_json
from scripts.utilitarios.logs import log_ok, log_warn, log_info

def main():
    log_info("🚀 Iniciando coleta_prefeitura_api")
    os.makedirs(DIR_PREFEITURA_API, exist_ok=True)
    endpoints = ["receitas", "despesas", "servidores", "obras", "contratos"]
    for endpoint in endpoints:
        for ano in ANOS:
            url = f"{URL_DADOS_ABERTOS_PREF}/api/{endpoint}?ano={ano}"
            out_path = os.path.join(DIR_PREFEITURA_API, f"{endpoint}_{ano}.json")
            sucesso = fetch_and_save_json(url, out_path)
            if not sucesso:
                log_warn(f"Falha na coleta JSON para {endpoint} {ano}")
    log_ok("✅ Coleta Prefeitura API finalizada")

if __name__ == "__main__":
    main()
