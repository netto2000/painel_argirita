"""
Nome: comparar_hierarquico.py
Finalidade: Comparar fontes processadas hierarquicamente e gerar resumo JSON
Autor: Fernando Neto
Data: 2025-10-05
"""

import os
import json
from scripts.config import DIR_PROCESSADOS
from scripts.utilitarios.logs import log_info, log_ok, log_warn

def percorrer_e_coletar_arquivos(base_path: str):
    arquivos = []
    for root, _, files in os.walk(base_path):
        for f in files:
            if f.endswith(".csv") or f.endswith(".txt"):
                caminho_completo = os.path.join(root, f)
                arquivos.append(os.path.relpath(caminho_completo, base_path))
    return arquivos

def main():
    log_info("🚀 Iniciando comparação hierárquica")
    resumo = {}
    for fonte in ["prefeitura", "camara", "tce"]:
        base = os.path.join(DIR_PROCESSADOS, fonte)
        if not os.path.exists(base):
            log_warn(f"Diretório base não existe: {base}")
            continue
        arquivos = percorrer_e_coletar_arquivos(base)
        resumo[fonte] = arquivos
        log_info(f"Fonte {fonte} tem {len(arquivos)} arquivos processados")

    out_path = os.path.join(DIR_PROCESSADOS, "comparacao_summary.json")
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(resumo, f, indent=2, ensure_ascii=False)
        log_ok(f"Resumo de comparação salvo em {out_path}")
    except Exception as e:
        log_warn(f"Falha ao salvar resumo JSON: {e}")

if __name__ == "__main__":
    main()
