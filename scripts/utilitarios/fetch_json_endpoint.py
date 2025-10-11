"""
fetch_json_endpoint.py
Função para requisitar JSON de um endpoint e salvar localmente,
com tratamento básico de erros e logs.
"""

import os
import requests
import os
import json
from scripts.utilitarios.logs import log_ok, log_warn
from scripts.config import ENCODING, TIMEOUT_REQUESTS

def fetch_and_save_json(url: str, out_path: str, headers=None, params=None) -> bool:
    try:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        # Segurança: verificação TLS ativa por padrão. Permite opt-out explícito via env var.
        verify_ssl = os.environ.get("ALLOW_INSECURE_HTTP", "0") not in {"1", "true", "True"}
        resp = requests.get(
            url,
            headers=headers or {},
            params=params or {},
            timeout=TIMEOUT_REQUESTS,
            verify=verify_ssl,
        )
        resp.raise_for_status()
        try:
            data = resp.json()
            with open(out_path, 'w', encoding=ENCODING) as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except json.JSONDecodeError:
            # Não é JSON válido, salva texto bruto
            with open(out_path, 'w', encoding=ENCODING) as f:
                f.write(resp.text)
            log_warn(f"Resposta não é JSON válido, texto salvo: {out_path}")
        log_ok(f"Salvo JSON: {out_path}")
        return True
    except Exception as e:
        log_warn(f"Falha na requisição {url}: {e}")
        return False
