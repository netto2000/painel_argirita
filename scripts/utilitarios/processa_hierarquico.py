"""
Nome: processa_hierarquico.py
Finalidade: Processar dados coletados hierarquicamente conforme as categorias definidas
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import json
import pandas as pd
from scripts.config import CATEGORIAS, DIR_BRUTOS, DIR_PROCESSADOS, ENCODING
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def processar_arquivo_json(caminho_arquivo: str):
    """
    Processa JSON, converte para CSV na pasta processados, mantendo hierarquia
    Retorna número de linhas processadas (0 em erro ou vazio)
    """
    if not os.path.exists(caminho_arquivo):
        log_warn(f"Arquivo não encontrado: {caminho_arquivo}")
        return 0
    try:
        with open(caminho_arquivo, "r", encoding=ENCODING) as f:
            conteudo = f.read()
            try:
                dados = json.loads(conteudo)
            except json.JSONDecodeError:
                log_warn(f"Arquivo não é JSON válido: {caminho_arquivo}")
                return 0
        if not dados:
            log_warn(f"Arquivo vazio: {caminho_arquivo}")
            return 0
        df = pd.DataFrame(dados)
        # Montar caminho para salvar csv
        rel_path = os.path.relpath(caminho_arquivo, DIR_BRUTOS)
        pasta_saida = os.path.join(DIR_PROCESSADOS, os.path.dirname(rel_path))
        os.makedirs(pasta_saida, exist_ok=True)
        nome_csv = os.path.join(pasta_saida, os.path.basename(caminho_arquivo).replace(".json", ".csv"))
        df.to_csv(nome_csv, index=False, encoding=ENCODING)
        log_ok(f"Processado e salvo CSV: {nome_csv} ({len(df)} linhas)")
        return len(df)
    except Exception as e:
        log_warn(f"Erro processamento {caminho_arquivo}: {e}")
        return 0

def percorrer_e_processar(base_path: str):
    """
    Navega recursivamente no diretório base_path da coleta brutos para processar todos JSONs encontrados
    """
    total_linhas = 0
    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith(".json"):
                caminho = os.path.join(root, f)
                linhas = processar_arquivo_json(caminho)
                total_linhas += linhas
    log_info(f"Total linhas processadas em {base_path}: {total_linhas}")
    return total_linhas

def main():
    log_info("🚀 Iniciando processamento hierárquico geral")
    linhas = percorrer_e_processar(DIR_BRUTOS)
    log_ok(f"✅ Processamento hierárquico finalizado, {linhas} linhas processadas")

if __name__ == "__main__":
    main()
