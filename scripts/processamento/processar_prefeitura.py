"""
Nome do Script: processar_prefeitura.py
Finalidade: Processa e limpa dados brutos coletados da Prefeitura Municipal.
Autor: Fernando Neto
Data: 2025-10-04
"""

import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def processar_dados_prefeitura():
    caminho_bruto = os.path.join("dados", "brutos", "prefeitura", "dados_prefeitura.json")
    caminho_processado = os.path.join("dados", "processados", "prefeitura")
    os.makedirs(caminho_processado, exist_ok=True)
    caminho_saida = os.path.join(caminho_processado, "dados_prefeitura_limpos.json")

    try:
        logging.info("Iniciando processamento dos dados da Prefeitura...")
        with open(caminho_bruto, "r", encoding="utf-8") as f:
            dados = json.load(f)
        dados_filtrados = [registro for registro in dados if registro.get("id") is not None]
        with open(caminho_saida, "w", encoding="utf-8") as f:
            json.dump(dados_filtrados, f, indent=2, ensure_ascii=False)
        logging.info(f"Dados da Prefeitura processados e salvos em {caminho_saida}")
    except Exception as e:
        logging.error(f"Erro ao processar dados da Prefeitura: {e}")

if __name__ == "__main__":
    processar_dados_prefeitura()
