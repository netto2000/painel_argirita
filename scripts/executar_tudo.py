"""
Nome do Script: executar_tudo.py
Finalidade: Executa todas as etapas do projeto na ordem correta.
Autor: Fernando Neto
Data: 2025-10-04
"""

import subprocess
import sys
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def executar_script(caminho_script):
    try:
        logging.info(f"Executando {caminho_script}...")
        result = subprocess.run([sys.executable, caminho_script], check=True)
        logging.info(f"Execução de {caminho_script} concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro na execução de {caminho_script}: {e}")

if __name__ == "__main__":
    scripts = [
        "scripts\\coleta\\coleta_camara_api_real.py",
        "scripts\\coleta\\coleta_prefeitura_api.py",
        "scripts\\processamento\\processar_camara.py",
        "scripts\\processamento\\processar_prefeitura.py",
        "scripts\\comparacao\\comparar_fontes.py",
        "scripts\\auditoria\\auditoria_regras.py",
        "scripts\\visualizacao\\dashboard_main.py"
    ]

    for script in scripts:
        executar_script(script)
