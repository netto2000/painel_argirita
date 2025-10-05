"""
coleta_hierarquica.py
Percorre a hierarquia de categorias e faz a coleta hierárquica dos dados.
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
from scripts.config import CATEGORIAS, DIR_PREFEITURA_API
from scripts.utilitarios.fetch_json_endpoint import fetch_and_save_json
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def percorrer_e_coletar(categorias: dict, base_path: str):
    """
    Percorre recursivamente a estrutura de categorias e realiza coleta das URLs.
    :param categorias: a hierarquia das categorias (dicionário aninhado)
    :param base_path: pasta base para salvar os arquivos coletados
    """
    for chave, valor in categorias.items():
        if isinstance(valor, dict):
            novo_path = os.path.join(base_path, chave)
            percorrer_e_coletar(valor, novo_path)
        elif isinstance(valor, str):
            os.makedirs(base_path, exist_ok=True)
            caminho = os.path.join(base_path, f"{chave}.json")
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
