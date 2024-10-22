import fitz
from bs4 import BeautifulSoup
import os

def pdf_to_html(pdf_path, html_path):
    # Abre o arquivo PDF
    pdf_document = fitz.open(pdf_path)
    html_content = ""

    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        text = page.get_text("text")
        images = page.get_images(full=True)

        # Constrói o conteúdo HTML
        # html_content += f"<h1>Página {page_num + 1}</h1>\n"
        html_content += "<div class='questoes'>\n"

        # Processa o texto para capturar questões e imagens
        lines = text.splitlines()
        for line in lines:
            if "QUESTÃO" in line:
                html_content += f"<h2>{line.strip()}</h2>\n"
            else:
                html_content += f"<p>{line.strip()}</p>\n"

        # Adiciona as imagens
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Salva a imagem
            image_path = f"imagem_pdf/image_{page_num + 1}_{img_index + 1}.{image_ext}"
            with open(image_path, "wb") as img_file:
                img_file.write(image_bytes)

            # Adiciona a imagem ao HTML
            html_content += f'<img src="{image_path}" alt="Imagem {img_index + 1}">\n'

        html_content += "</div>\n"

    # Fecha o documento PDF
    pdf_document.close()

    # Gera o arquivo HTML
    with open(html_path, "w", encoding="utf-8") as html_file:
        soup = BeautifulSoup(html_content, "html.parser")
        html_file.write(soup.prettify())

# Caminhos dos arquivos
pdf_file_path = "/home/enock/projects/alura_vileve/python/start_python/scrap_enem/microdados_enem_2023/PROVAS E GABARITOS/LEITOR_TELA/ENEM_2023_P1_CAD_09_DIA_1_LARANJA_LEITOR_TELA_NVDA_LC.pdf"  # Atualize para o caminho do seu PDF
html_file_path = "output.html"  # Caminho de saída do arquivo HTML

# Converte o PDF para HTML
pdf_to_html(pdf_file_path, html_file_path)
print(f"Arquivo HTML gerado em: {html_file_path}")