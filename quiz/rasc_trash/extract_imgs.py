import fitz  # PyMuPDF
import os

# Caminho do arquivo PDF
pdf_path = "/home/enock/projects/alura_vileve/python/start_python/scrap_enem/microdados_enem_2023/PROVAS E GABARITOS/LEITOR_TELA/ENEM_2023_P1_CAD_09_DIA_1_LARANJA_LEITOR_TELA_NVDA_LC.pdf"


# Diretório para armazenar as imagens extraídas
image_folder = "imagem_pdf"
os.makedirs(image_folder, exist_ok=True)

# Abrir o PDF
pdf_document = fitz.open(pdf_path)

for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)
    images = page.get_images(full=True)

    for img_index, img in enumerate(images):
        xref = img[0]
        base_image = pdf_document.extract_image(xref)
        image_bytes = base_image["image"]
        image_filename = f"imagem_pdf/pagina_{page_number + 1}_imagem_{img_index + 1}.png"

        # Salve a imagem
        with open(image_filename, "wb") as image_file:
            image_file.write(image_bytes)

print("Imagens extraídas com sucesso!")