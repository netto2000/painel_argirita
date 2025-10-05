"""
orquestrador.py
Executa passo a passo toda a cadeia de execução do projeto.
"""

import subprocess
import sys

def run_module(module_name):
    print(f"\nIniciando execução de {module_name}")
    process = subprocess.run([sys.executable, "-m", module_name], capture_output=True, text=True)
    print(process.stdout)
    if process.returncode != 0:
        print(f"Erro ao executar {module_name}:")
        print(process.stderr)
        sys.exit(process.returncode)

def main():
    sequencia = [
        "scripts.coleta.coleta_prefeitura_api",
        "scripts.coleta.coleta_camara_api_real",
        "scripts.coleta.coleta_tce",
        "scripts.coleta.coleta_hierarquica",  # corrigido pasta para coleta
        "scripts.processamento.processa_hierarquico",
        "scripts.comparacao.comparar_hierarquico",
        "scripts.verificacao.verificar_integridade_hierarquico"
    ]

    for modulo in sequencia:
        run_module(modulo)

    print("\nWorkflow completo executado com sucesso!")

if __name__ == "__main__":
    main()
