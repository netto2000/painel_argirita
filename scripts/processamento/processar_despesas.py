# -*- coding: utf-8 -*-
r"""
Nome do Script: processar_despesas.py
Finalidade: Agrupa/normaliza arquivos brutos de despesas para análise.
Autor: Fernando Neto
Data: 2025-10-05
"""

import json
import csv
from pathlib import Path
import logging

# Definições dos diretórios e encoding
DIR_BRUTOS = Path("dados/brutos/despesas")
DIR_PROCESSADOS = Path("dados/processados/despesas")
DIR_PROCESSADOS.mkdir(parents=True, exist_ok=True)
ENCODING = "utf-8"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def _concat_jsons(out_json, out_csv):
    rows = []
    files = sorted(DIR_BRUTOS.glob("*.json"))
    if not files:
        logging.warning("Nenhum arquivo JSON encontrado na pasta de dados brutos de despesas.")
        return False
    for f in files:
        try:
            logging.info(f"Lendo arquivo {f}")
            j = json.loads(f.read_text(encoding=ENCODING))
            if isinstance(j, dict) and "data" in j:
                data = j["data"]
                logging.info(f"Arquivo {f} contém 'data' com {len(data)} registros")
            elif isinstance(j, list):
                data = j
                logging.info(f"Arquivo {f} contém uma lista com {len(data)} registros")
            else:
                logging.warning(f"Formato inesperado no arquivo {f}, ignorando")
                data = []
            rows.extend(data)
        except Exception as e:
            logging.warning(f"Falha lendo {f}: {e}")

    if not rows:
        logging.warning("Nenhum registro encontrado após ler todos os arquivos.")
        return False

    logging.info(f"Total de registros agrupados: {len(rows)}")

    # Salva JSON consolidado
    with open(out_json, "w", encoding=ENCODING) as fh:
        json.dump(rows, fh, ensure_ascii=False, indent=2)

    # Extrai chaves para CSV
    keys = set()
    for r in rows:
        if isinstance(r, dict):
            keys.update(r.keys())
    keys = sorted(keys)

    # Salva CSV
    with open(out_csv, "w", encoding=ENCODING, newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=keys)
        writer.writeheader()
        for r in rows:
            if isinstance(r, dict):
                writer.writerow({k: r.get(k, "") for k in keys})
    logging.info(f"Gerado arquivo JSON e CSV em:\n{out_json}\n{out_csv}")
    return True

def main():
    logging.info("Início do processamento das despesas")
    _concat_jsons(DIR_PROCESSADOS / "despesas_processadas.json", DIR_PROCESSADOS / "despesas_processadas.csv")
    logging.info("Fim do processamento das despesas")

if __name__ == "__main__":
    main()
