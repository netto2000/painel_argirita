"""
Nome: config.py
Finalidade: Configurações e hierarquia de categorias
Autor: Fernando Neto
Data: 2025-10-05
"""

import os

DIR_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
ENCODING = "utf-8"
TIMEOUT_REQUESTS = 20
COD_IBGE = 3104403
ANOS = list(range(2017, 2026))

DIR_DADOS = os.path.join(DIR_BASE, "dados")
DIR_BRUTOS = os.path.join(DIR_DADOS, "brutos")
DIR_PROCESSADOS = os.path.join(DIR_DADOS, "processados")
DIR_LOGS = os.path.join(DIR_BASE, "logs")

DIR_PREFEITURA_API = os.path.join(DIR_BRUTOS, "prefeitura", "api")
DIR_CAMARA_API = os.path.join(DIR_BRUTOS, "camara", "api")
DIR_TCE_PORTAL = os.path.join(DIR_BRUTOS, "tce", "portal")

URL_DADOS_ABERTOS_PREF = "https://dadosabertos-portalfacil.azurewebsites.net/16"
URL_DADOS_ABERTOS_CAMARA = "https://cm-argirita.publicacao.siplanweb.com.br"
URL_DADOS_ABERTOS_TCE = "https://www.tce.mg.gov.br/Painel"

CATEGORIAS = {
    "Receitas": {
        "Receitas_orcamentarias": {
            "Detalhada_por_dia": "https://transparencia.argirita.mg.gov.br/receitas-por-dias",
            "Detalhada_por_meses": {
                "Correntes": "https://transparencia.argirita.mg.gov.br/tpc_rec_mes_vis.aspx?exercicio=2025&idReceita=1.0.0.0.00.00.00&dsReceita=Receitas%20Correntes",
                "De_Capital": "https://transparencia.argirita.mg.gov.br/tpc_rec_mes_vis.aspx?exercicio=2025&idReceita=2.0.0.0.00.00.00&dsReceita=Receitas%20De%20Capital",
                "Deducoes": "https://transparencia.argirita.mg.gov.br/tpc_rec_mes_vis.aspx?exercicio=2025&idReceita=9.0.0.0.00.00.00&dsReceita=Dedu%C3%A7%C3%B5es%20De%20Receitas",
            },
            "Extraorcamentaria": "https://transparencia.argirita.mg.gov.br/extraorcamentarias/tipo/receitas/r"
        }
    },
    # (Continue preenchendo outras categorias conforme necessidade)
}
