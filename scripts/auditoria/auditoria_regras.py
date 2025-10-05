"""
Nome do Script: auditoria_regras.py
Finalidade: Define regras de auditoria para validação dos dados.
Autor: Fernando Neto
Data: 2025-10-04
"""

import os
import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def validar_dados_camara():
    caminho = os.path.join("dados", "processados", "camara", "dados_camara_limpos.json")
    try:
        logging.info("Iniciando auditoria dos dados da Câmara...")
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)

        # Exemplo básico de regra: campo obrigatório 'valor' deve ser positivo
        erros = []
        for i, registro in enumerate(dados):
            if "valor" not in registro or registro["valor"] <= 0:
                erros.append(f"Registro {i} com valor inválido: {registro}")

        if erros:
            logging.warning(f"Erros encontrados na auditoria: {len(erros)}")
            for erro in erros:
                logging.warning(erro)
        else:
            logging.info("Auditoria concluída sem erros.")

    except Exception as e:
        logging.error(f"Erro na auditoria: {e}")

if __name__ == "__main__":
    validar_dados_camara()
