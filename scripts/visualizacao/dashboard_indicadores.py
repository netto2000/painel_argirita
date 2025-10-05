"""
dashboard_indicadores.py
Dashboard interativo para indicadores consolidados do Painel_Argirita via Streamlit.
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import streamlit as st
import pandas as pd
from scripts.config import DIR_PROCESSADOS, ENCODING
from scripts.utilitarios.logs import log_warn

st.set_page_config(page_title="Dashboard Indicadores", layout="wide")
st.title("📈 Dashboard Indicadores Consolidados")

def carregar_indicadores():
    caminho = os.path.join(DIR_PROCESSADOS, "indicadores", "indicadores_gerais.csv")
    if not os.path.exists(caminho):
        log_warn(f"Arquivo indicadores não encontrado: {caminho}")
        st.warning(f"Arquivo indicadores não encontrado: {caminho}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(caminho, encoding=ENCODING)
        return df
    except Exception as e:
        st.error(f"Erro ao carregar indicadores: {e}")
        return pd.DataFrame()

def main():
    df = carregar_indicadores()
    if df.empty:
        st.info("Nenhum indicador disponível para exibição.")
        return

    anos = df['Ano'].unique()
    ano_selecionado = st.sidebar.selectbox("Selecione o Ano", sorted(anos))
    df_ano = df[df['Ano'] == ano_selecionado]

    st.subheader(f"Indicadores para o ano {ano_selecionado}")
    st.dataframe(df_ano)

    indicadores_plot = df.set_index('Ano').drop(columns=['Ano'])
    st.line_chart(indicadores_plot)

if __name__ == "__main__":
    main()
