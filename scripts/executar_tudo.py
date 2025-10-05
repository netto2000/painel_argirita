"""
Nome do Script: executar_tudo.py
Finalidade: Executa em sequência todos os scripts do projeto, garantindo importação correta dos módulos.
Autor: Fernando Neto
Data: 2025-10-05
"""

import sys
import os
import subprocess
import logging

# Configura o logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Adiciona a raiz do projeto no sys.path para importação dos pacotes
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Função para executar scripts Python via subprocess
def executar_script(script_module):
    logging.info(f"Executando {script_module}...")
    try:
        # Executa com python -m para usar namespace correto
        subprocess.run([sys.executable, "-m", script_module], check=True)
        logging.info(f"Execução de {script_module} concluída com sucesso.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Erro na execução de {script_module}: {e}")

def main():
    # Ordem dos módulos para execução
    scripts = [
        "scripts.coleta.coleta_camara_api_real",
        "scripts.coleta.coleta_prefeitura_api",
        "scripts.processamento.processar_camara",
        "scripts.processamento.processar_prefeitura",
        "scripts.comparacao.comparar_fontes",
        "scripts.auditoria.auditoria_regras",
        # O dashboard não é chamado aqui pois é interface interativa
    ]

    for script in scripts:
        executar_script(script)

if __name__ == "__main__":
    main()
