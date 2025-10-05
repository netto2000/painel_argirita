# -*- coding: utf-8 -*-
"""
Nome do Script: selenium_chromedriver_raspagem.py
Finalidade: Raspagem de dados do portal transparência Argirita com Selenium e webdriver_manager
Autor: Fernando Neto
Data: 2025-10-05
"""

import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

URL = "https://transparencia.argirita.mg.gov.br/servidores"

def iniciar_driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def esperar_elemento(driver, by, seletor, timeout=20):
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, seletor)))

def extrair_tabela(html):
    soup = BeautifulSoup(html, 'html.parser')
    tabela = soup.find('table')
    if not tabela:
        print("Tabela não encontrada no HTML.")
        return []

    headers = [th.get_text(strip=True) for th in tabela.find_all('th')]
    rows = []
    for tr in tabela.find_all('tr')[1:]:
        cols = tr.find_all('td')
        if not cols:
            continue
        row = {headers[i]: cols[i].get_text(strip=True) for i in range(len(cols))}
        rows.append(row)
    return rows

def main():
    driver = iniciar_driver()
    print("Abrindo página...")
    driver.get(URL)

    try:
        print("Esperando tabela carregar...")
        tabela_elemento = esperar_elemento(driver, By.CSS_SELECTOR, 'table', timeout=30)
        html_tabela = tabela_elemento.get_attribute('outerHTML')

        print("Extraindo dados da tabela...")
        dados = extrair_tabela(html_tabela)

        print(f"Total de registros extraídos: {len(dados)}")
        with open('dados_webscraping_servidores.json', 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print("Dados salvos em dados_webscraping_servidores.json")

    except Exception as e:
        print(f"Erro na extração: {e}")

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
