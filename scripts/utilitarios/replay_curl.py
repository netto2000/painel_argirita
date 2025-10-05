# -*- coding: utf-8 -*-
"""
Nome do Script: replay_curl.py
Finalidade:    Função utilitária para replicar requisições web (como as capturadas do navegador)
               e extrair dados JSON de endpoints. É o nosso "canivete suíço" de coleta.
Autor:         Fernando Neto
Data:          2025-10-04
"""

import requests
import json
import os

def extrair_dados_endpoint(url, headers, payload=None, nome_arquivo_saida=None, diretorio_saida="dados\\brutos"):
    """
    Executa uma requisição POST ou GET para um endpoint e salva a resposta JSON.

    Args:
        url (str): A URL do endpoint.
        headers (dict): O dicionário de cabeçalhos da requisição.
        payload (dict, optional): Os dados a serem enviados no corpo da requisição POST. Defaults to None.
        nome_arquivo_saida (str, optional): O nome do arquivo para salvar os dados. Se None, imprime na tela.
        diretorio_saida (str, optional): O diretório relativo onde o arquivo será salvo. Defaults to "dados\\brutos".

    Returns:
        bool: True se a requisição foi bem-sucedida, False caso contrário.
    """
    print(f"🚀 Tentando conectar ao endpoint: {url}")

    try:
        # Define o método com base na existência de um payload
        if payload:
            print("   - Método: POST")
            response = requests.post(url, headers=headers, data=payload, timeout=30)
        else:
            print("   - Método: GET")
            response = requests.get(url, headers=headers, timeout=30)
        
        # Verifica se a requisição foi bem-sucedida
        response.raise_for_status()
        print("✅ Conexão bem-sucedida!")

        # Tenta extrair o JSON da resposta
        try:
            dados_json = response.json()
            print("📊 Dados JSON extraídos com sucesso.")

            # Se um nome de arquivo foi fornecido, salva os dados
            if nome_arquivo_saida:
                # Garante que o diretório de saída exista
                if not os.path.exists(diretorio_saida):
                    os.makedirs(diretorio_saida)
                
                caminho_completo = os.path.join(diretorio_saida, nome_arquivo_saida)
                
                with open(caminho_completo, 'w', encoding='utf-8') as f:
                    json.dump(dados_json, f, ensure_ascii=False, indent=4)
                
                print(f"✅ Dados salvos com sucesso em: {caminho_completo}")
            else:
                # Se não, apenas imprime os dados formatados
                print(json.dumps(dados_json, ensure_ascii=False, indent=4))
            
            return True

        except json.JSONDecodeError:
            print("⚠️ A resposta não é um JSON válido. Conteúdo da resposta:")
            print(response.text[:500]) # Mostra os primeiros 500 caracteres
            return False

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro de conexão: {e}")
        return False