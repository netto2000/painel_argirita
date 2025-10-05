"""
relatorio_consolidado.py
Geração de relatórios consolidados a partir dos indicadores financeiros municipais.
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import pandas as pd
from scripts.config import DIR_PROCESSADOS, ENCODING
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def carregar_indicadores():
    caminho = os.path.join(DIR_PROCESSADOS, "indicadores", "indicadores_gerais.csv")
    if not os.path.exists(caminho):
        log_warn(f"Arquivo indicadores não encontrado: {caminho}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(caminho, encoding=ENCODING)
        log_ok(f"Indicadores carregados de {caminho}")
        return df
    except Exception as e:
        log_warn(f"Erro ao carregar indicadores: {e}")
        return pd.DataFrame()

def gerar_resumo_geral(df_indicadores: pd.DataFrame) -> pd.DataFrame:
    """
    Gera resumo geral com médias, mínimos, máximos, e contagem.
    """
    if df_indicadores.empty:
        log_warn("Dataframe de indicadores vazio")
        return df_indicadores

    resumo = df_indicadores.describe(include='all').transpose()
    resumo['Contagem'] = df_indicadores.count()
    resumo = resumo.rename(columns={
        'mean': 'Média',
        'min': 'Mínimo',
        '25%': '1º Quartil',
        '50%': 'Mediana',
        '75%': '3º Quartil',
        'max': 'Máximo'
    })
    log_ok("Resumo estatístico geral gerado")
    return resumo

def salvar_relatorio(df_resumo: pd.DataFrame):
    pasta = os.path.join(DIR_PROCESSADOS, "relatorios")
    os.makedirs(pasta, exist_ok=True)
    caminho = os.path.join(pasta, "resumo_geral_indicadores.csv")
    try:
        df_resumo.to_csv(caminho, encoding=ENCODING)
        log_ok(f"Relatório consolidado salvo em {caminho}")
    except Exception as e:
        log_warn(f"Erro ao salvar relatório: {e}")

def main():
    log_info("🚀 Iniciando geração de relatório consolidado")
    df = carregar_indicadores()
    if df.empty:
        log_warn("Nenhum dado para gerar relatório consolidado")
        return
    resumo = gerar_resumo_geral(df)
    salvar_relatorio(resumo)

if __name__ == '__main__':
    main()
