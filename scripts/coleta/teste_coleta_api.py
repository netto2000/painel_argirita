# -*- coding: utf-8 -*-
"""
Nome do Script: teste_coleta_api.py
Finalidade: Testar coleta básica de API no projeto Painel_Argirita
Autor: Fernando Neto
Data: 2025-10-05
"""

import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ID_CLIENTE = 16
BASE_URL = "https://dadosabertos-portalfacil.azurewebsites.net/16/"

def testar_api(endpoint):
    params = {
        "numAno": 2025,
        "idCliente": ID_CLIENTE,
        "type": "json",
        "page": 1,
        "pageSize": 10
    }
    url = BASE_URL + endpoint
    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()
        registros = data.get("data", [])
        logging.info(f"[{endpoint}] registros na página 1: {len(registros)}")
        if registros:
            exemplo = registros[0]
            logging.info(f"Exemplo registro {endpoint}: {exemplo}")
        else:
            logging.warning(f"Nenhum registro encontrado para {endpoint}")
    except Exception as e:
        logging.error(f"Erro na chamada API {endpoint}: {e}")

def main():
    endpoints = [
        "despesas",
        "receitas",
        "servidores"
    ]
    for ep in endpoints:
        testar_api(ep)

if __name__ == "__main__":
    main()
