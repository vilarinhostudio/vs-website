import os
import argparse

TEMPLATE = """\
---
title: {img_name}
draft: false
cover: "[[../assets/{folder_name}/{img_name}.png]]"
---

![{img_name}](../assets/{folder_name_encoded}/{img_name}.png)
"""

def main():
   parser = argparse.ArgumentParser(
       description="Gera notas .md para cada imagem PNG em ./assets/<folder_img>."
   )
   parser.add_argument(
       "folder_img",
       help="Nome da pasta dentro de ./content/assets/ (ex: galeria)"
   )
   args = parser.parse_args()

   gallery_dir = os.path.abspath(os.path.join(".", "content", "assets", args.folder_img))
   folder_name = args.folder_img
   folder_name_encoded = folder_name.replace(" ", "%20")
   img_md_dir = os.path.join(gallery_dir, "img_md")

   if not os.path.isdir(gallery_dir):
       print(f"Erro: diretório não encontrado: {gallery_dir}")
       return

   os.makedirs(img_md_dir, exist_ok=True)
   print(f"Pasta criada: {img_md_dir}")

   images = [f for f in os.listdir(gallery_dir) if f.lower().endswith(".png")]

   if not images:
       print("Nenhuma imagem PNG encontrada.")
       return

   for img_file in images:
       img_name = os.path.splitext(img_file)[0]
       md_content = TEMPLATE.format(
           img_name=img_name,
           folder_name=folder_name,
           folder_name_encoded=folder_name_encoded
       )
       md_path = os.path.join(img_md_dir, f"{img_name}.md")

       with open(md_path, "w", encoding="utf-8") as f:
           f.write(md_content)

       print(f"  Criado: {img_name}.md")

   print(f"\nConcluído: {len(images)} nota(s) gerada(s) em '{img_md_dir}'")

if __name__ == "__main__":
   main()
