"""
Nome do Script: dashboard_main.py
Finalidade: Script principal do dashboard Streamlit para visualização dos dados.
Autor: Fernando Neto
Data: 2025-10-04
"""

import streamlit as st
import os
import json

def carregar_dados_camara():
    caminho = os.path.join("dados", "processados", "camara", "dados_camara_limpos.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def carregar_dados_prefeitura():
    caminho = os.path.join("dados", "processados", "prefeitura", "dados_prefeitura_limpos.json")
    with open(caminho, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    st.title("Painel de Fiscalização de Argirita")
    st.subheader("Dados da Câmara Municipal")
    dados_camara = carregar_dados_camara()
    st.write(f"Número de registros: {len(dados_camara)}")
    st.json(dados_camara[:5])

    st.subheader("Dados da Prefeitura Municipal")
    dados_prefeitura = carregar_dados_prefeitura()
    st.write(f"Número de registros: {len(dados_prefeitura)}")
    st.json(dados_prefeitura[:5])

if __name__ == "__main__":
    main()
