Painel Argirita - Projeto de Análise Financeira e Fiscal Municipal
Sumário
Visão Geral
Estrutura do Projeto
Configuração do Ambiente
Fluxo de Execução
Módulos Principais
Indicadores Financeiros
Dashboard Interativo
Contribuição e Contato

Visão Geral
Projeto para coletar, processar e analisar dados financeiros, contábeis e fiscais do município de Argirita (MG), com o objetivo de gerar indicadores para suporte à fiscalização pública via dashboards e relatórios consolidados.

Estrutura do Projeto
text
Painel_Argirita/
├── dados/
│   ├── brutos/             # Dados coletados brutos em JSON, HTML etc
│   ├── processados/        # Dados transformados, em CSV
│   ├── indicadores/        # Indicadores financeiros calculados
│   ├── relatorios/         # Relatórios consolidados gerados
├── logs/                   # Logs de execução dos scripts
├── scripts/
│   ├── coleta/             # Scripts para coleta de dados
│   ├── processamento/      # Processamento e transformação de dados
│   ├── comparacao/         # Comparações entre dados e versões
│   ├── verificacao/        # Verificações e auditorias de integridade
│   ├── analise/            # Geração de indicadores financeiros
│   ├── exportacao/         # Geração de relatórios consolidados
│   ├── visualizacao/       # Dashboards Streamlit e interfaces interativas
│   ├── utilitarios/        # Funções e helpers reutilizáveis
│   ├── orquestrador.py     # Script para execução completa do fluxo
├── tests/                  # Testes unitários e funcionais (planejado)
├── venv/                   # Ambiente virtual Python
├── requirements.txt        # Dependências do projeto
└── README.md               # Este arquivo
Configuração do Ambiente
Clonar o repositório e entrar no diretório do projeto.

Criar e ativar o ambiente virtual Python (recomendado Python 3.10+):

bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
Instalar dependências:

bash
pip install -r requirements.txt
Fluxo de Execução
Para rodar todo o fluxo integrado (coleta, processamento, análise, exportação e verificação), use o orquestrador:

bash
python scripts/orquestrador.py
Isso executa na ordem:

Coleta de dados (prefeitura, câmara, TCE)

Processamento hierárquico (JSON para CSV)

Geração de indicadores financeiros

Geração de relatórios consolidados

Verificação da integridade dos dados

Módulos Principais
scripts/coleta/ - extração dos dados públicos das fontes oficiais

scripts/processamento/ - limpeza e transformação dos dados

scripts/analise/gerar_indicadores.py - cálculos dos indicadores financeiros e fiscais

scripts/exportacao/relatorio_consolidado.py - gera resumos estatísticos para análise

scripts/visualizacao/dashboard_indicadores.py - dashboard interativo via Streamlit

scripts/utilitarios/ - utilitários de logs, salvamento, requisições

Indicadores Financeiros
O módulo de indicadores contempla:

Liquidez Corrente

Grau de Endividamento (em desenvolvimento)

Resultado Primário

Receita Própria vs Receita Total

Despesa com Pessoal / Receita Corrente Líquida

Aplicação em Educação (%)

Aplicação em Saúde (%)

Dashboard Interativo
Para visualizar os indicadores em dashboard:

bash
streamlit run scripts/visualizacao/dashboard_indicadores.py
Os dados são atualizados após a execução do módulo de indicadores.

Contribuição e Contato
Para dúvidas, melhorias ou contribuições:

[E-mail do responsável do projeto]

[Repositório GitHub - link]

Este README serve como roteiro diário para manter foco e continuidade do projeto Painel_Argirita.

