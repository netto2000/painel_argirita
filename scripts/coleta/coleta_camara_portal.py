# -*- coding: utf-8 -*-
"""
Nome do Script: coleta_camara_portal.py
Finalidade:    Coleta dados de Receitas Orçamentárias diretamente do endpoint do 
               Portal da Transparência da Câmara Municipal de Argirita.
Autor:         Fernando Neto
Data:          2025-10-04
"""

# Importa nossa ferramenta de coleta
from scripts.utilitarios.replay_curl import extrair_dados_endpoint

def coletar_receitas_orcamentarias_camara(ano):
    """
    Busca os dados de receitas orçamentárias da Câmara para um ano específico.
    """
    print(f"\n--- 📊 Iniciando coleta de Receitas da Câmara para o ano de {ano} ---")

    # URL do endpoint que retorna os dados (você descobriu isso!) [cite: 7696, 7821, 8050]
    url = "https://cm-argirita.publicacao.siplanweb.com.br/contas-receitas/grid-receitas"

    # Cabeçalhos da requisição (copiados da sua análise com F12) [cite: 7699-7721]
    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://cm-argirita.publicacao.siplanweb.com.br",
        "referer": "https://cm-argirita.publicacao.siplanweb.com.br/contas-receitas",
        "x-csrf-token": "2hzXsMUWDswkbUkZv0f3oGH7v1e9AGozfqY93Y5H",
        "x-requested-with": "XMLHttpRequest",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36",
    }

    # Payload (corpo) da requisição para buscar todos os dados do ano (-1 no 'length') [cite: 7723, 7839]
    payload = {
        "exercicio": ano,
        "length": "-1" # Pedimos todos os registros de uma vez
    }

    # Nome do arquivo de saída
    nome_arquivo = f"camara_receitas_orcamentarias_{ano}.json"
    diretorio_saida = "dados\\brutos\\camara"

    # Chama nossa ferramenta para fazer o trabalho sujo
    sucesso = extrair_dados_endpoint(
        url=url, 
        headers=headers, 
        payload=payload, 
        nome_arquivo_saida=nome_arquivo,
        diretorio_saida=diretorio_saida
    )
    
    if sucesso:
        print(f"--- ✅ Coleta de Receitas da Câmara para {ano} concluída! ---")
    else:
        print(f"--- ⚠️ Falha na coleta de Receitas da Câmara para {ano}. ---")


if __name__ == "__main__":
    # Podemos definir aqui os anos que queremos buscar
    anos_para_coletar = range(2017, 2026) # De 2017 até 2025

    for ano in anos_para_coletar:
        coletar_receitas_orcamentarias_camara(ano)