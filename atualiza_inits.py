import os

def criar_init_vazio(caminho):
    init_path = os.path.join(caminho, "__init__.py")
    if not os.path.exists(init_path):
        with open(init_path, "w", encoding="utf-8") as f:
            f.write("# Init file")
        print(f"[OK] Criado: {init_path}")
    else:
        print(f"[EXISTE] {init_path}")

def loop_pastas(dir_base):
    for root, dirs, files in os.walk(dir_base):
        if "venv" in root:
            continue
        criar_init_vazio(root)

if __name__ == '__main__':
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "scripts")
    print(f"Iniciando criação de __init__.py em pastas sob {base}")
    loop_pastas(base)
    print("Finalizado.")
