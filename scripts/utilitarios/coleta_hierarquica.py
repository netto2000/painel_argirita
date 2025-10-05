"""
Nome: coleta_hierarquica.py
Finalidade: Funções para percorrer hierarquia e coletar dados
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
from typing import Union
from scripts.config import CATEGORIAS, DIR_PREFEITURA_API, ENCODING, TIMEOUT_REQUESTS
from scripts.utilitarios.fetch_json_endpoint import fetch_and_save_json
from scripts.utilitarios.logs import log_info, log_ok, log_warn
import requests

def percorrer_e_coletar(categorias: dict, base_path: str):
    """
    Percorre recursivamente o dicionário de categorias e coleta dados das URLs.
    :param categorias: dicionário aninhado de categorias e URLs
    :param base_path: diretório base para salvamento dos dados
    """
    for chave, valor in categorias.items():
        if isinstance(valor, dict):
            # hierarquia continua, cria subdiretório e continua recursão
            novo_path = os.path.join(base_path, chave)
            percorrer_e_coletar(valor, novo_path)
        elif isinstance(valor, str):
            # valor é URL, realizar coleta e salvar JSON
            os.makedirs(base_path, exist_ok=True)
            nome_arquivo = f"{chave}.json"
            caminho = os.path.join(base_path, nome_arquivo)
            log_info(f"Iniciando coleta: {chave} -> {valor}")
            sucesso = fetch_and_save_json(valor, caminho)
            if sucesso:
                log_ok(f"Coleta concluída: {caminho}")
            else:
                log_warn(f"Falha na coleta: {caminho}")
        else:
            log_warn(f"Tipo inesperado em {chave}: {type(valor)}")

def main():
    log_info("🚀 Iniciando coleta hierárquica geral")
    percorrer_e_coletar(CATEGORIAS, DIR_PREFEITURA_API)
    log_ok("✅ Coleta hierárquica concluída")

if __name__ == "__main__":
    main()
