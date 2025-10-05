"""
gerar_indicadores.py
Cálculo de indicadores financeiros, contábeis e fiscais para o Painel_Argirita.
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import pandas as pd
from scripts.config import DIR_PROCESSADOS, ENCODING
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def carregar_dados(tipo: str, ano: int) -> pd.DataFrame:
    """
    Carrega dados processados por tipo (ex: receitas, despesas) e ano.
    """
    pasta = os.path.join(DIR_PROCESSADOS, tipo)
    arquivo = os.path.join(pasta, f"{tipo}_{ano}.csv")
    if not os.path.exists(arquivo):
        log_warn(f"Arquivo não encontrado: {arquivo}")
        return pd.DataFrame()
    try:
        df = pd.read_csv(arquivo, encoding=ENCODING)
        return df
    except Exception as e:
        log_warn(f"Erro ao carregar {arquivo}: {e}")
        return pd.DataFrame()

def calcular_indicadores(ano: int) -> dict:
    """
    Calcula os indicadores para o ano dado, retornando dicionário com os resultados.
    """
    indicadores = {}

    # Carregar dados
    receitas = carregar_dados('receitas', ano)
    despesas = carregar_dados('despesas', ano)
    pessoal = carregar_dados('servidores', ano)  # Exemplo simplificado

    try:
        receita_corrente_liquida = receitas.get('Receita Corrente Líquida', pd.Series([0])).sum()
        despesas_pessoal = despesas.get('Despesa com Pessoal', pd.Series([0])).sum()
        receita_propria = receitas.get('Receita Própria', pd.Series([0])).sum()
        despesa_total = despesas.get('Despesa Total', pd.Series([0])).sum()
        aplic_educacao = despesas.get('Aplicação em Educação', pd.Series([0])).sum()
        aplic_saude = despesas.get('Aplicação em Saúde', pd.Series([0])).sum()
        resultado_primario = receitas.get('Receita Total', pd.Series([0])).sum() - despesas.get('Despesa Primária', pd.Series([0])).sum()

        # Indicadores principais
        indicadores['Ano'] = ano
        indicadores['Liquidez Corrente'] = receita_corrente_liquida / despesa_total if despesa_total else None
        indicadores['Grau de Endividamento'] = None  # preciso dos dados de dívida para calcular
        indicadores['Resultado Primário'] = resultado_primario
        indicadores['Receita Própria / Receita Total'] = receita_propria / receitas.get('Receita Total', pd.Series([0])).sum() if receitas.get('Receita Total', pd.Series([0])).sum() else None
        indicadores['Despesa com Pessoal / Receita Corrente Líquida'] = despesas_pessoal / receita_corrente_liquida if receita_corrente_liquida else None
        indicadores['Aplicação em Educação (%)'] = (aplic_educacao / receita_corrente_liquida * 100) if receita_corrente_liquida else None
        indicadores['Aplicação em Saúde (%)'] = (aplic_saude / receita_corrente_liquida * 100) if receita_corrente_liquida else None

        log_ok(f"Indicadores calculados para o ano {ano}")

    except Exception as e:
        log_warn(f"Erro no cálculo dos indicadores para o ano {ano}: {e}")

    return indicadores

def gerar_indicadores_para_anos(anos):
    resultados = []
    for ano in anos:
        ind = calcular_indicadores(ano)
        if ind:
            resultados.append(ind)
    return pd.DataFrame(resultados)

def main():
    anos = list(range(2017, 2026))
    log_info("🚀 Iniciando geração de indicadores hierárquicos")
    df_indicadores = gerar_indicadores_para_anos(anos)
    if not df_indicadores.empty:
        out_path = os.path.join(DIR_PROCESSADOS, 'indicadores', 'indicadores_gerais.csv')
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        df_indicadores.to_csv(out_path, index=False, encoding=ENCODING)
        log_ok(f"Indicadores hierárquicos salvos em {out_path}")
    else:
        log_warn("Nenhum indicador gerado")

if __name__ == '__main__':
    main()
