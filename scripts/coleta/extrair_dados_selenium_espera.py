# -*- coding: utf-8 -*-
"""
Nome do Script: extrair_dados_selenium_espera.py
Finalidade: Extrair dados do portal da transparência de Argirita simulando navegação com espera de elementos.
Autor: Fernando Neto
Data: 2025-10-05
"""

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://transparencia.argirita.mg.gov.br/servidores"

def iniciar_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    return driver

def extrair_dados():
    driver = iniciar_driver()
    driver.get(URL)

    try:
        wait = WebDriverWait(driver, 15)  # aguardar até 15 segundos
        # Ajustar seletor conforme a estrutura da página real, exemplo busca a primeira tabela
        tabela = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
        )
    except Exception as e:
        print(f"Erro ao localizar tabela na página: {e}")
        driver.quit()
        return

    html = tabela.get_attribute('outerHTML')
    driver.quit()

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    headers = [th.get_text(strip=True) for th in soup.find_all('th')]
    rows = []
    for tr in soup.find_all('tr')[1:]:
        cols = tr.find_all('td')
        if not cols:
            continue
        row = {headers[i]: cols[i].get_text(strip=True) for i in range(len(cols))}
        rows.append(row)

    with open('dados_brutos_servidores.json', 'w', encoding='utf-8') as f:
        json.dump(rows, f, ensure_ascii=False, indent=2)

    print(f"Extração finalizada: {len(rows)} registros salvos em dados_brutos_servidores.json")

if __name__ == "__main__":
    extrair_dados()
