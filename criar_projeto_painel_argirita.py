# -*- coding: utf-8 -*-
"""
Nome do Script: criar_projeto_painel_argirita.py
Finalidade:    Cria a estrutura completa de diretórios e arquivos para o novo projeto 'Painel_Argirita'.
Autor:         Seu Assistente AI
Data:          2025-10-04
"""

import os
from datetime import datetime

def criar_estrutura_projeto(caminho_base):
    """
    Cria uma estrutura de diretórios e arquivos para o projeto 'Painel_Argirita'.
    
    Argumento:
        caminho_base (str): O caminho raiz onde a estrutura do projeto será criada.
    """
    print("🚀 Iniciando a construção do seu novo projeto: Painel_Argirita...")

    # Definição da estrutura de pastas baseada no seu mapa
    diretorios = [
        ".pytest_cache",
        "dados/brutos/camara", "dados/brutos/prefeitura", "dados/brutos/siconfi", "dados/brutos/tce",
        "dados/indicadores",
        "dados/processados/camara", "dados/processados/prefeitura", "dados/processados/tce",
        "logs",
        "scripts/analise", "scripts/auditoria", "scripts/coleta", "scripts/comparacao",
        "scripts/exportacao", "scripts/portal", "scripts/processamento", "scripts/utilitarios",
        "scripts/verificacao", "scripts/visualizacao",
        "tests",
        "venv/Scripts" # Apenas a pasta essencial para o activate.bat
    ]

    # Definição dos arquivos a serem criados
    arquivos_python = {
        "scripts/__init__.py": "",
        "scripts/config.py": "",
        "scripts/executar_tudo.py": "Ponto de entrada para execução completa.",
        "scripts/analise/__init__.py": "",
        "scripts/auditoria/__init__.py": "",
        "scripts/auditoria/auditoria_regras.py": "Define as regras de auditoria dos dados.",
        "scripts/coleta/__init__.py": "",
        "scripts/coleta/coleta_all.py": "Orquestra todas as coletas de dados.",
        "scripts/coleta/coleta_camara_api_real.py": "Coleta dados da API da Câmara.",
        "scripts/coleta/coleta_camara_portal.py": "Faz scraping dos dados do portal da Câmara.",
        "scripts/coleta/coleta_prefeitura_api.py": "Coleta dados da API da Prefeitura.",
        "scripts/coleta/coleta_prefeitura_portal.py": "Faz scraping dos dados do portal da Prefeitura.",
        "scripts/coleta/coleta_siconfi.py": "Coleta dados do SICONFI.",
        "scripts/coleta/coleta_tce.py": "Coleta dados do TCE.",
        "scripts/comparacao/__init__.py": "",
        "scripts/comparacao/comparar_fontes.py": "Compara dados de diferentes fontes.",
        "scripts/exportacao/__init__.py": "",
        "scripts/exportacao/gerar_relatorio_pdf.py": "Gera relatórios em PDF.",
        "scripts/portal/__init__.py": "",
        "scripts/processamento/__init__.py": "",
        "scripts/processamento/processar_all.py": "Orquestra todo o processamento de dados.",
        "scripts/processamento/processar_camara.py": "Processa e limpa dados da Câmara.",
        "scripts/processamento/processar_prefeitura.py": "Processa e limpa dados da Prefeitura.",
        "scripts/processamento/processar_tce.py": "Processa e limpa dados do TCE.",
        "scripts/utilitarios/__init__.py": "",
        "scripts/utilitarios/atualizar_cod_ibge.py": "Funções para atualizar códigos IBGE.",
        "scripts/utilitarios/logs.py": "Configuração centralizada de logs.",
        "scripts/verificacao/__init__.py": "",
        "scripts/verificacao/diagnostico_sistema.py": "Verifica a saúde e dependências do sistema.",
        "scripts/verificacao/verificar_integridade.py": "Verifica a integridade dos dados coletados.",
        "scripts/visualizacao/__init__.py": "",
        "scripts/visualizacao/dashboard_main.py": "Script principal do dashboard Streamlit.",
        "tests/__init__.py": "",
        "tests/test_coleta_siconfi.py": "Testes unitários para a coleta do SICONFI."
    }
    
    outros_arquivos = {
        "README.md": "# Painel de Fiscalização de Argirita-MG\n\nEste projeto centraliza a coleta, processamento e visualização de dados públicos do município de Argirita-MG.",
        "requirements.txt": "# Liste aqui as dependências do projeto, ex: pandas\nstreamlit\nrequests\n",
        "executar.bat": "",
        "abrir_vscode.ps1": "code .",
        r"venv\Scripts\activate.bat": "@echo off\n" # Arquivo essencial para o ambiente virtual
    }

    # 1. Cria o diretório raiz do projeto
    try:
        os.makedirs(caminho_base, exist_ok=True)
        print(f"✅ Diretório principal '{caminho_base}' criado com sucesso.")
    except OSError as e:
        print(f"❌ Erro ao criar o diretório principal: {e}")
        return

    # 2. Cria todos os subdiretórios
    for d in diretorios:
        caminho_completo = os.path.join(caminho_base, d.replace('/', os.sep))
        os.makedirs(caminho_completo, exist_ok=True)
        print(f"  - Pasta criada: {d}")

    # 3. Cria os arquivos .py com o cabeçalho padrão
    data_hoje = datetime.now().strftime("%Y-%m-%d")
    for caminho_relativo, finalidade in arquivos_python.items():
        caminho_completo = os.path.join(caminho_base, caminho_relativo.replace('/', os.sep))
        nome_arquivo = os.path.basename(caminho_completo)
        
        docstring = f'''"""
Nome do Script: {nome_arquivo}
Finalidade:    {finalidade if finalidade else "Módulo de inicialização."}
Autor:         Fernando Neto
Data:          {data_hoje}
"""
'''
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(docstring.strip())
        print(f"  - Arquivo .py criado: {caminho_relativo}")

    # 4. Cria os outros arquivos com conteúdo inicial
    for caminho_relativo, conteudo in outros_arquivos.items():
        caminho_completo = os.path.join(caminho_base, caminho_relativo.replace('\\', os.sep))
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        print(f"  - Arquivo criado: {caminho_relativo}")

    print("\n\n✅ Estrutura do projeto 'Painel_Argirita' finalizada com sucesso!")
    print("Pode abrir a pasta no VS Code e começar a trabalhar.")

if __name__ == '__main__':
    # Define o caminho base onde o projeto será criado.
    diretorio_documentos = os.path.expanduser("~\\Documents")
    caminho_do_projeto = os.path.join(diretorio_documentos, "Painel_Argirita")
    
    # Executa a função principal
    criar_estrutura_projeto(caminho_do_projeto)