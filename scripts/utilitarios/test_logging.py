"""
Nome: test_logging.py
Finalidade: Testar o sistema unificado de logs do Painel_Argirita
Autor: Fernando Neto
Data: 2025-10-05
"""

from scripts.utilitarios.logs import log_info, log_ok, log_warn, log_error

def main():
    log_info("Iniciando teste de logging...")
    log_ok("Teste de log OK executado com sucesso.")
    log_warn("Este é um aviso de teste.")
    log_error("Esta é uma mensagem de erro de teste.")
    print("Teste de logs concluído! Verifique o terminal e o arquivo logs/fiscalizacao.log")

if __name__ == "__main__":
    main()
