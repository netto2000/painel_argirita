"""
verificar_integridade_hierarquico.py
Verificação de diretórios essenciais do projeto.
"""

import os
from scripts.config import DIR_BRUTOS, DIR_PROCESSADOS, DIR_LOGS
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def verificar_dir(path: str) -> bool:
    if os.path.exists(path):
        log_ok(f"{path} → Presente")
        return True
    else:
        log_warn(f"{path} → Ausente")
        return False

def main():
    log_info("🚀 Iniciando verificação hierárquica de integridade")
    for base_dir in [DIR_BRUTOS, DIR_PROCESSADOS, DIR_LOGS]:
        verificar_dir(base_dir)
    for fonte in ["prefeitura", "camara", "tce"]:
        verificar_dir(os.path.join(DIR_BRUTOS, fonte))
        verificar_dir(os.path.join(DIR_PROCESSADOS, fonte))
    log_ok("✅ Verificação de integridade concluída")

if __name__ == "__main__":
    main()
