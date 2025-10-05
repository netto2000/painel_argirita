"""
dashboard_hierarquico.py
Dashboard interativo com Streamlit mostrando hierarquia dos dados.
"""

import os
import streamlit as st
import pandas as pd
from scripts.config import CATEGORIAS, DIR_PROCESSADOS, ENCODING
from scripts.utilitarios import logs

st.set_page_config(page_title="Dashboard Hierárquico", layout="wide")
st.title("📊 Dashboard Hierárquico — Fiscalização Argirita")

def buscar_csv_pasta(caminho_base, caminho_categoria):
    csv_potential = os.path.join(caminho_base, caminho_categoria + ".csv")
    if os.path.exists(csv_potential):
        return csv_potential
    return None

def carregar_csv(caminho_csv):
    try:
        df = pd.read_csv(caminho_csv, encoding=ENCODING)
        return df
    except Exception as e:
        return f"Erro ao carregar CSV: {e}"

def main():
    fonte = "prefeitura"  # pode implementar escolha dinâmica
    ano = st.sidebar.selectbox("Ano", list(range(2017, 2026)))
    
    # Navegação hierárquica simples
    nivel1 = st.sidebar.selectbox("Categoria N1", list(CATEGORIAS.keys()))
    nivel1_data = CATEGORIAS[nivel1]

    if isinstance(nivel1_data, dict):
        nivel2 = st.sidebar.selectbox("Categoria N2", list(nivel1_data.keys()))
        nivel2_data = nivel1_data[nivel2]
        if isinstance(nivel2_data, dict):
            nivel3 = st.sidebar.selectbox("Categoria N3", list(nivel2_data.keys()))
            selecionado = nivel3
        else:
            selecionado = nivel2
    else:
        selecionado = nivel1

    caminho_csv = buscar_csv_pasta(
        os.path.join(DIR_PROCESSADOS, fonte),
        selecionado.replace("_", " ")
    )

    if caminho_csv:
        dados = carregar_csv(caminho_csv)
        if isinstance(dados, pd.DataFrame):
            st.dataframe(dados.head(100), use_container_width=True)
            st.metric("Linhas", len(dados))
        else:
            st.error(dados)
    else:
        st.info("Nenhum dado encontrado para esta seleção.")

if __name__ == "__main__":
    main()
