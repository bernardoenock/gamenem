from pdfminer.high_level import extract_text

# Caminho do arquivo PDF
pdf_path = "/home/enock/projects/alura_vileve/python/start_python/scrap_enem/microdados_enem_2023/PROVAS E GABARITOS/LEITOR_TELA/ENEM_2023_P1_CAD_09_DIA_1_LARANJA_LEITOR_TELA_NVDA_LC.pdf"

# Extrair texto do PDF
pdf_text = extract_text(pdf_path)

# Dividir o texto em questões com base no padrão 'QUESTÃO'
# 01 - 05 linguas


print(pdf_text)

# # Percorrer as questões extraídas
# questoes_html = ""
# for i, questao in enumerate(questoes[1:], 1):  # Pula o primeiro elemento, pois é antes das questões
#     questoes_html += f"<h2>Questão {i}</h2>\n"
#     questoes_html += f"<p>{questao}</p>\n"
    
#     # Adiciona as opções de resposta (radio buttons)
#     for opcao in ['A', 'B', 'C', 'D', 'E']:
#         questoes_html += f"""
#         <label><input type="radio" name="q{i}" value="{opcao}"> {opcao}</label><br>
#         """

# print("Texto das questões extraído com sucesso.")


# from pdf2image import convert_from_path
# import os

# # Diretório para armazenar as imagens das questões
# image_folder = "enem_images"
# os.makedirs(image_folder, exist_ok=True)

# # Converter as páginas do PDF em imagens
# pages = convert_from_path(pdf_path)

# # Salvar as imagens das questões específicas (por exemplo, página 3, 5...)
# image_paths = []
# questao_imagem_mapping = {1: [1], 3: [5]}  # Mapeamento de questão para páginas de imagens (exemplo)
# for questao, page_numbers in questao_imagem_mapping.items():
#     for page_num in page_numbers:
#         image_path = os.path.join(image_folder, f"questao_{questao}_page_{page_num}.png")
#         pages[page_num-1].save(image_path, "PNG")
#         image_paths.append((questao, image_path))

# print("Imagens extraídas e salvas com sucesso.")


# # Gerar o HTML completo
# html_with_images = """
# <!DOCTYPE html>
# <html lang="pt-BR">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Prova ENEM 2023 - Questões</title>
# </head>
# <body>
#     <h1>Prova ENEM 2023 - Questões</h1>
# """

# # Adicionar as questões e as imagens no HTML
# for i, questao in enumerate(questoes[1:], 1):
#     html_with_images += f"<h2>Questão {i}</h2>\n"
#     html_with_images += f"<p>{questao}</p>\n"
    
#     # Se houver imagens associadas à questão, adicioná-las
#     for questao_num, img_path in image_paths:
#         if questao_num == i:
#             html_with_images += f'<img src="{img_path}" alt="Imagem da Questão {i}" style="width:100%;">\n'
    
#     # Adicionar opções de resposta (radio buttons)
#     for opcao in ['A', 'B', 'C', 'D', 'E']:
#         html_with_images += f"""
#         <label><input type="radio" name="q{i}" value="{opcao}"> {opcao}</label><br>
#         """

# html_with_images += """
# </body>
# </html>
# """

# # Salvar o HTML
# with open("prova_enem_2023_com_questoes_e_imagens.html", "w") as file:
#     file.write(html_with_images)

# print("HTML com questões e imagens criado com sucesso.")
