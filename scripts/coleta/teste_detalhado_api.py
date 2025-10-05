import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = "https://dadosabertos-portalfacil.azurewebsites.net/16/despesas"
PARAMS = {
    "numAno": 2023,
    "idCliente": 16,
    "type": "json",
    "page": 1,
    "pageSize": 100
}

def main():
    try:
        response = requests.get(URL, params=PARAMS, timeout=10)
        logging.info(f"Status HTTP: {response.status_code}")
        logging.info(f"Headers da resposta: {response.headers}")
        if response.content:
            logging.info(f"Conteúdo da resposta: {response.content[:500]} (exibindo até 500 bytes)")
            try:
                data = response.json()
                logging.info(f"JSON carregado com sucesso. Chaves principais: {list(data.keys())}")
            except Exception as e:
                logging.error(f"Erro ao decodificar JSON: {e}")
        else:
            logging.warning("Conteúdo da resposta vazio")
    except Exception as e:
        logging.error(f"Erro na requisição: {e}")

if __name__ == "__main__":
    main()
