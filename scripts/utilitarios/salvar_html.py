"""
salvar_html.py
Função para salvar HTML em arquivo com encoding e logs.
"""

import os
from scripts.utilitarios.logs import log_ok, log_warn
from scripts.config import ENCODING

def salvar_html(path: str, content: str) -> bool:
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, 'w', encoding=ENCODING) as f:
            f.write(content)
        log_ok(f"Salvo HTML: {path}")
        return True
    except Exception as e:
        log_warn(f"Falha ao salvar HTML {path}: {e}")
        return False
