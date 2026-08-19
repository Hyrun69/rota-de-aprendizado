import os
import shutil

print("--- Rota de Aprendizado: Organizador Inteligente ---")

pasta_origem = "materiais"
pasta_destino = "organizado"

if not os.path.exists(pasta_origem):
    os.makedirs(pasta_origem)

if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

categorias = {
    ".pdf": "Documentos_PDF",
    ".jpg": "Imagens",
    ".png": "Imagens",
    ".docx": "Trabalhos_Escola",
    ".txt": "Notas"
}

ficheiros = os.listdir(pasta_origem)
contador = 0

for f in ficheiros:
    nome, extensao = os.path.splitext(f)
    extensao = extensao.lower()

    if extensao in categorias:
        subpasta = categorias[extensao]
        caminho_subpasta = os.path.join(pasta_destino, subpasta)

        if not os.path.exists(caminho_subpasta):
            os.makedirs(caminho_subpasta)

        # Lógica para evitar apagar duplicados
        caminho_final = os.path.join(caminho_subpasta, f)
        base_nome = nome
        n = 1
        
        # Se o ficheiro já existir, muda o nome (ex: foto.jpg -> foto_1.jpg)
        while os.path.exists(caminho_final):
            caminho_final = os.path.join(caminho_subpasta, f"{base_nome}_{n}{extensao}")
            n += 1

        shutil.move(os.path.join(pasta_origem, f), caminho_final)
        print(f"[OK] Organizado: {os.path.basename(caminho_final)}")
        contador += 1

print(f"--- Sucesso! {contador} ficheiros organizados sem perdas. ---")
