"""
Nome: coleta_camara_api_real.py
Finalidade: Coleta dados reais da Câmara via API
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import requests
from scripts.config import DIR_CAMARA_API, URL_DADOS_ABERTOS_CAMARA, TIMEOUT_REQUESTS
from scripts.utilitarios.logs import log_ok, log_warn, log_info

URLS = {
    "header_links_uteis": f"{URL_DADOS_ABERTOS_CAMARA}/header/links-uteis",
    "header_menu_selecionado": f"{URL_DADOS_ABERTOS_CAMARA}/header/menu-selecionado",
    "header_estrutura_organizacional": f"{URL_DADOS_ABERTOS_CAMARA}/header/estrutura-organizacional",
    "header_conheca_portal": f"{URL_DADOS_ABERTOS_CAMARA}/header/conheca-portal",
    "verificar_sessao": f"{URL_DADOS_ABERTOS_CAMARA}/verificar-sessao"
}

def main():
    log_info("🚀 Iniciando coleta_camara_api_real")
    os.makedirs(DIR_CAMARA_API, exist_ok=True)
    session = requests.Session()
    session.headers.update({
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept": "application/json, text/plain, */*",
        "Referer": f"{URL_DADOS_ABERTOS_CAMARA}/dados-abertos/consulta"
    })

    # Segurança: verificação TLS ativa por padrão; permite opt-out explícito via env.
    verify_ssl = os.environ.get("ALLOW_INSECURE_HTTP", "0") not in {"1", "true", "True"}

    for nome, url in URLS.items():
        out_path = os.path.join(DIR_CAMARA_API, f"{nome}.json")
        try:
            resp = session.post(url, timeout=TIMEOUT_REQUESTS, verify=verify_ssl)
            if resp.status_code == 405 or not resp.text:
                resp = session.get(url, timeout=TIMEOUT_REQUESTS, verify=verify_ssl)
            resp.raise_for_status()
            try:
                data = resp.json()
                with open(out_path, "w", encoding="utf-8") as f:
                    import json
                    json.dump(data, f, ensure_ascii=False, indent=2)
            except Exception:
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(resp.text)
            log_ok(f"Salvo {nome} em {out_path}")
        except Exception as e:
            log_warn(f"Falha ao coletar {nome}: {e}")

    log_ok("✅ Coleta Câmara API finalizada")

if __name__ == "__main__":
    main()
