# -*- coding: utf-8 -*-
"""
Nome do Script: extrair_dados_selenium.py
Finalidade: Extrair dados do portal da transparência de Argirita simulando navegação.
Autor: Fernando Neto
Data: 2025-10-05
"""

import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

URL = "https://transparencia.argirita.mg.gov.br/servidores"

def iniciar_driver():
    options = Options()
    options.add_argument('--headless')  # Rodar sem abrir janela física
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

def extrair_dados():
    driver = iniciar_driver()
    driver.get(URL)
    time.sleep(5)  # Tempo para a página carregar e executar scripts JS

    # Pega a página renderizada com dados
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html, 'html.parser')
    
    # Localize aqui a tabela de dados
    tabela = soup.find('table')
    if not tabela:
        print("Tabela não encontrada na página.")
        return

    # Extrai cabeçalho
    headers = []
    for th in tabela.find_all('th'):
        headers.append(th.get_text(strip=True))

    # Extrai dados
    rows = []
    for tr in tabela.find_all('tr')[1:]:
        cols = tr.find_all('td')
        if len(cols) == 0:
            continue
        row = {}
        for i, td in enumerate(cols):
            row[headers[i]] = td.get_text(strip=True)
        rows.append(row)

    # Salva em JSON local
    with open('dados_brutos_servidores.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)
    
    print(f"Extração concluída, {len(rows)} registros salvos em dados_brutos_servidores.json")

if __name__ == "__main__":
    extrair_dados()
