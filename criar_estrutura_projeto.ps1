import os

def criar_estrutura_projeto(caminho_base):
    """
    Cria uma estrutura de diretórios e arquivos para o projeto.

    Argumento:
        caminho_base (str): O caminho raiz onde a estrutura do projeto será criada.
    """
    # Lista de todos os diretórios a serem criados
    diretorios = [
        ".pytest_cache/v/cache",
        "dados/brutos/camara",
        "dados/brutos/prefeitura",
        "dados/brutos/siconfi",
        "dados/brutos/tce",
        "dados/indicadores",
        "dados/processados/camara",
        "dados/processados/prefeitura",
        "dados/processados/tce",
        "logs",
        "scripts/__pycache__",
        "scripts/analise",
        "scripts/auditoria/__pycache__",
        "scripts/coleta/__pycache__",
        "scripts/comparacao/__pycache__",
        "scripts/exportacao",
        "scripts/portal",
        "scripts/processamento/__pycache__",
        "scripts/utilitarios/__pycache__",
        "scripts/verificacao/__pycache__",
        "scripts/visualizacao",
        "tests/__pycache__",
        "venv/etc/jupyter",
        "venv/Include",
        "venv/Lib/site-packages",
        "venv/Scripts",
        "venv/share/jupyter",
    ]

    # Lista de todos os arquivos vazios a serem criados
    arquivos = [
        "abrir_powershell.ps1",
        "abrir_vscode.ps1",
        "coleta_siconfi.py",
        "executar.ps1",
        "explore-codigos.ps1",
        "habilitar_pwsh7_contexto.ps1",
        "README.md",
        "requirements.txt",
        "show-estrutura.ps1",
        "scripts/__init__.py",
        "scripts/config.py",
        "scripts/executar_tudo.py",
        "scripts/analise/__init__.py",
        "scripts/auditoria/__init__.py",
        "scripts/auditoria/auditoria_regras.py",
        "scripts/coleta/__init__.py",
        "scripts/coleta/coleta_all.py",
        "scripts/coleta/coleta_camara_api_real.py",
        "scripts/coleta/coleta_camara_portal.py",
        "scripts/coleta/coleta_prefeitura_api.py",
        "scripts/coleta/coleta_prefeitura_portal.py",
        "scripts/coleta/coleta_siconfi.py",
        "scripts/coleta/coleta_tce.py",
        "scripts/comparacao/__init__.py",
        "scripts/comparacao/comparar_fontes.py",
        "scripts/exportacao/__init__.py",
        "scripts/exportacao/gerar_relatorio_pdf.py",
        "scripts/portal/__init__.py",
        "scripts/processamento/__init__.py",
        "scripts/processamento/processar_all.py",
        "scripts/processamento/processar_camara.py",
        "scripts/processamento/processar_prefeitura.py",
        "scripts/processamento/processar_tce.py",
        "scripts/utilitarios/__init__.py",
        "scripts/utilitarios/atualizar_cod_ibge.py",
        "scripts/utilitarios/create_sample_data.py",
        "scripts/utilitarios/criar_logs.py",
        "scripts/utilitarios/fetch_json_endpoint.py",
        "scripts/utilitarios/fix_imports.py",
        "scripts/utilitarios/limpar_logs.py",
        "scripts/utilitarios/logs.py",
        "scripts/utilitarios/replay_curl.py",
        "scripts/utilitarios/salvar_html.py",
        "scripts/verificacao/__init__.py",
        "scripts/verificacao/diagnostico_sistema.py",
        "scripts/verificacao/fixar_estrutura.py",
        "scripts/verificacao/verificar_integridade.py",
        "scripts/visualizacao/__init__.py",
        "scripts/visualizacao/dashboard_geral.py",
        "scripts/visualizacao/dashboard_main.py",
        "scripts/visualizacao/dashboard_orcamento.py",
        "scripts/visualizacao/dashboard_pessoal.py",
        "scripts/visualizacao/dashboard_principal.py",
        "scripts/visualizacao/dashboard.py",
        "tests/test_coleta_siconfi.py",
    ]

    # Cria o diretório raiz do projeto
    try:
        os.makedirs(caminho_base, exist_ok=True)
        print(f"Diretório principal '{caminho_base}' criado com sucesso.")
    except OSError as e:
        print(f"Erro ao criar o diretório principal: {e}")
        return

    # Cria todos os subdiretórios
    for d in diretorios:
        caminho_completo = os.path.join(caminho_base, d)
        try:
            os.makedirs(caminho_completo, exist_ok=True)
            print(f"  - Diretório criado: {caminho_completo}")
        except OSError as e:
            print(f"Erro ao criar o diretório {caminho_completo}: {e}")

    # Cria todos os arquivos vazios
    for a in arquivos:
        caminho_completo = os.path.join(caminho_base, a)
        try:
            with open(caminho_completo, 'w') as f:
                pass  # Cria um arquivo vazio
            print(f"  - Arquivo criado: {caminho_completo}")
        except OSError as e:
            print(f"Erro ao criar o arquivo {caminho_completo}: {e}")

if __name__ == '__main__':
    # Define o caminho base para o novo projeto
    caminho_do_projeto = r"C:\Users\nando\Documents\Painel_Argirita"
    
    # Executa a função para criar a estrutura
    criar_estrutura_projeto(caminho_do_projeto)
    print("\nEstrutura do projeto 'Painel_Argirita' criada com sucesso!")