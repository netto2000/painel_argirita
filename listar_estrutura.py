import os

def listar_estrutura(diretorio, prefixo=''):
    try:
        conteudo = sorted(os.listdir(diretorio))
    except PermissionError:
        return
    for item in conteudo:
        caminho_item = os.path.join(diretorio, item)
        if os.path.isdir(caminho_item):
            print(f"{prefixo}[DIR] {item}")
            listar_estrutura(caminho_item, prefixo + "    ")
        else:
            print(f"{prefixo}{item}")

if __name__ == "__main__":
    raiz = '.'  # Diretório atual, onde o script está
    print("Estrutura do projeto Painel_Argirita:")
    listar_estrutura(raiz)
