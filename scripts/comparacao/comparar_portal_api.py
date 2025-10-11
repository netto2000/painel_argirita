"""
comparar_portal_api.py
Compara quantitativos básicos entre:
- Azure Open Data (dadosabertos-portalfacil) vs Prefeitura API (URL_DADOS_ABERTOS_PREF)
- Portal Câmara (arquivo bruto salvo) vs Câmara API (quando disponível)

Gera um resumo JSON em dados/processados/comparacao/resumo_comparacao.json
"""

import os
import json
from glob import glob
from scripts.config import DIR_BRUTOS, DIR_PROCESSADOS, ENCODING
from scripts.utilitarios.logs import log_info, log_ok, log_warn


def _contar_registros_json(path_pattern: str) -> int:
    total = 0
    for file_path in glob(path_pattern):
        try:
            with open(file_path, 'r', encoding=ENCODING) as f:
                data = json.load(f)
            if isinstance(data, dict) and 'data' in data and isinstance(data['data'], list):
                total += len(data['data'])
            elif isinstance(data, list):
                total += len(data)
            else:
                # fallback: tenta interpretar como lista de linhas em string JSON
                total += 1
        except Exception as e:
            log_warn(f"Falha lendo {file_path}: {e}")
    return total


def main():
    log_info("🚀 Iniciando comparação portal vs API")
    resumo = {
        'prefeitura': {},
        'camara': {}
    }

    # Prefeitura
    dir_pref_api = os.path.join(DIR_BRUTOS, 'prefeitura')
    dir_pref_azure = os.path.join('dados', 'brutos')

    # Considera endpoints coletados pelo coleta_all.py
    endpoints = ['despesas', 'receitas', 'contratos', 'licitacoes', 'servidores']
    for ep in endpoints:
        azure_path = os.path.join(dir_pref_azure, ep, '*.json')
        api_path = os.path.join(dir_pref_api, f'{ep}_*.json')
        resumo['prefeitura'][ep] = {
            'azure_open_data_registros': _contar_registros_json(azure_path),
            'api_prefeitura_registros': _contar_registros_json(api_path)
        }

    # Câmara
    dir_camara_brutos = os.path.join(DIR_BRUTOS, 'camara')
    camara_portal_path = os.path.join(dir_camara_brutos, 'camara_receitas_orcamentarias_*.json')
    resumo['camara']['portal_receitas_orcamentarias'] = _contar_registros_json(camara_portal_path)

    # Local de saída
    out_dir = os.path.join(DIR_PROCESSADOS, 'comparacao')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'resumo_comparacao.json')

    with open(out_file, 'w', encoding=ENCODING) as f:
        json.dump(resumo, f, ensure_ascii=False, indent=2)

    log_ok(f"Resumo salvo em {out_file}")


if __name__ == '__main__':
    main()
