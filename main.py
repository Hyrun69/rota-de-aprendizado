import os
import shutil

print("--- Rota de Aprendizado: Organizador Iniciado ---")

# 1. Definir as pastas
pasta_origem = "materiais"
pasta_destino = "organizado"

# 2. Criar as pastas se elas não existirem
if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)
    print(f"Pasta '{pasta_origem}' criada. Coloca lá os teus ficheiros desarrumados!")

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# 3. Mapear extensões para pastas específicas
categorias = {
    ".pdf": "Documentos_PDF",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".docx": "Trabalhos_Escola",
    ".txt": "Notas"
}

# 4. A "Magia": Percorrer os ficheiros e organizar
ficheiros = os.listdir(pasta_origem)
contador = 0

for f in ficheiros:
    # Separar o nome da extensão (ex: "trabalho" e ".pdf")
    nome, extensao = os.path.splitext(f)
    extensao = extensao.lower()

    if extensao in categorias:
        subpasta = categorias[extensao]
        caminho_subpasta = os.path.join(pasta_destino, subpasta)

        # Criar a subpasta (ex: organizado/Documentos_PDF) se não existir
        if not os.path.exists(caminho_subpasta):
            os.makedirs(caminho_subpasta)

        # Mover o ficheiro da origem para o destino
        shutil.move(os.path.join(pasta_origem, f), os.path.join(caminho_subpasta, f))
        print(f"[OK] Movido: {f} -> {subpasta}")
        contador += 1

print(f"--- Fim da tarefa. {contador} ficheiros organizados! ---")
