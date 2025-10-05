"""
Nome do Script: comparar_fontes.py
Finalidade: Compara dados de fontes diferentes para identificar divergências.
Autor: Fernando Neto
Data: 2025-10-04
"""

import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def comparar_camara_prefeitura():
    caminho_camara = os.path.join("dados", "processados", "camara", "dados_camara_limpos.json")
    caminho_prefeitura = os.path.join("dados", "processados", "prefeitura", "dados_prefeitura_limpos.json")

    try:
        logging.info("Iniciando comparação de dados entre Câmara e Prefeitura...")
        with open(caminho_camara, "r", encoding="utf-8") as f_camara:
            dados_camara = json.load(f_camara)
        with open(caminho_prefeitura, "r", encoding="utf-8") as f_prefeitura:
            dados_prefeitura = json.load(f_prefeitura)

        ids_camara = set(reg.get("id") for reg in dados_camara)
        ids_prefeitura = set(reg.get("id") for reg in dados_prefeitura)

        ids_nao_comuns = (ids_camara - ids_prefeitura).union(ids_prefeitura - ids_camara)
        if ids_nao_comuns:
            logging.warning(f"IDs divergentes encontrados: {len(ids_nao_comuns)}")
        else:
            logging.info("Nenhuma divergência de IDs encontrada entre as fontes.")

    except Exception as e:
        logging.error(f"Erro na comparação: {e}")

if __name__ == "__main__":
    comparar_camara_prefeitura()
