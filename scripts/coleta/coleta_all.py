"""
Nome do Script: coleta_all.py
Finalidade: Coleta automatizada de múltiplas categorias de dados públicos do portal de Transparência Municipal de Argirita.
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import json
import logging
import requests
from datetime import datetime

# Configurações globais de logging e parâmetros da API
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
ID_CLIENTE = 16  # Código IBGE ou código cliente para Argirita conforme documentação
ANO_INICIAL = 2017
ANO_FINAL = datetime.now().year

BASE_URL_TEMPLATE = "https://dadosabertos-portalfacil.azurewebsites.net/16/{endpoint}"

def salvar_json(dados, arquivo):
    os.makedirs(os.path.dirname(arquivo), exist_ok=True)
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
    logging.info(f"Arquivo salvo: {arquivo}")

def coletar_categoria(endpoint: str, nome_arquivo: str, ano_inicio=ANO_INICIAL, ano_fim=ANO_FINAL):
    dados_completos = []
    
    for ano in range(ano_inicio, ano_fim + 1):
        logging.info(f"Coletando '{endpoint}' do ano {ano}...")
        pagina = 1
        while True:
            params = {
                "numAno": ano,
                "idCliente": ID_CLIENTE,
                "type": "json",
                "page": pagina,
                "pageSize": 100
            }
            url = BASE_URL_TEMPLATE.format(endpoint=endpoint)
            try:
                response = requests.get(url, params=params, timeout=30)
                response.raise_for_status()

                if response.status_code == 204 or not response.content:
                    logging.warning(f"Resposta vazia para {endpoint}, ano {ano}, página {pagina}. Finalizando esta coleta.")
                    break

                try:
                    dados = response.json()
                except json.JSONDecodeError:
                    logging.error(f"Resposta inválida (não-JSON) para {endpoint}, ano {ano}, página {pagina}.")
                    break

                registros = dados.get("data", [])
                if not registros:
                    logging.info(f"Nenhum registro para {endpoint}, ano {ano}, página {pagina}.")
                    break

                dados_completos.extend(registros)
                total_paginas = dados.get("last_page", 1)
                logging.info(f"{endpoint} - Ano {ano} Página {pagina}/{total_paginas} - Registros: {len(registros)}")

                if pagina >= total_paginas:
                    break
                pagina += 1

            except requests.RequestException as e:
                logging.error(f"Erro ao coletar {endpoint}, ano {ano}, página {pagina}: {e}")
                break

    caminho_arquivo = os.path.join("dados", "brutos", endpoint, nome_arquivo)
    salvar_json(dados_completos, caminho_arquivo)


def main():
    categorias = {
        "despesas": "despesas.json",
        "receitas": "receitas.json",
        "contratos": "contratos.json",
        "licitacoes": "licitacoes.json",
        "servidores": "servidores.json"
    }
    for endpoint, arquivo in categorias.items():
        coletar_categoria(endpoint, arquivo)


if __name__ == "__main__":
    main()
