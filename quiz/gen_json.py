import fitz
import json
import os
import re

def extract_questions_from_pdf(pdf_path, output_image_dir, output_json_path):
    # Abre o PDF
    pdf_document = fitz.open(pdf_path)
    
    # Dicionário para armazenar as questões
    questions = []
    
    # Cria o diretório de saída de imagens, se não existir
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    
    # Variáveis para controle de questões e conteúdo
    current_question = None
    current_content = []
    options = {}
    current_images = []  # Para armazenar as imagens da questão atual
    
    # Percorre as páginas do PDF
    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text = page.get_text("text")
        images = page.get_images(full=True)
        
        # Divide o texto da página em linhas
        lines = text.split("\n")
        line_index = 0  # Índice para percorrer as linhas
        
        while line_index < len(lines):
            line = lines[line_index].strip()
            
            # Verifica se a linha contém uma nova questão
            if "QUESTÃO" in line:
                if current_question:
                    # Salva a questão anterior antes de começar a nova
                    questions.append({
                        "title": current_question,
                        "content": " ".join(current_content).strip(),
                        "options": options,
                        "images": current_images  # Adiciona as imagens acumuladas
                    })
                
                # Inicializa uma nova questão
                current_question = line.strip()
                current_content = []
                options = {}
                current_images = []  # Reseta a lista de imagens para a nova questão

            # Identifica as opções (a., b., c., d., e.)
            elif re.match(r"^[a-e]\.\s", line):  # Verifica se a linha começa com a letra da opção
                option_letra = line[0]
                option_content = line[2:].strip()
                
                # Adiciona a opção ao dicionário
                if option_letra in "abcde":
                    options[option_letra] = option_content

                # Acumula opções se necessário
                while True:
                    line_index += 1  # Avança para a próxima linha
                    if line_index < len(lines):
                        next_line = lines[line_index].strip()
                        # Verifica se a próxima linha é uma nova opção
                        if re.match(r"^[a-e]\.\s", next_line):
                            option_letra = next_line[0]
                            option_content = next_line[2:].strip()
                            options[option_letra] = option_content
                            break  # Sai do loop se encontrou uma nova opção
                        else:
                            option_content += " " + next_line  # Continua acumulando
                    else:
                        break

                # Certifica-se de que a opção acumulada é adicionada corretamente
                if option_letra in "abcde" and option_content:
                    options[option_letra] = option_content.strip()

            else:
                # Considera as linhas como parte do enunciado da questão
                current_content.append(line.strip())
            
            line_index += 1  # Avança para a próxima linha
        
        # Adiciona as imagens da página
        for image_index, img in enumerate(images):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_ext = base_image["ext"]
            
            # Salva a imagem no diretório
            image_filename = f"image_{page_num + 1}_{image_index + 1}.{image_ext}"
            image_path = os.path.join(output_image_dir, image_filename)
            with open(image_path, "wb") as img_file:
                img_file.write(base_image["image"])
            
            # Armazena o caminho da imagem na lista current_images
            current_images.append(image_path)
    
    # Salva a última questão
    if current_question:
        questions.append({
            "title": current_question,
            "content": " ".join(current_content).strip(),
            "options": options,
            "images": current_images  # Adiciona as imagens acumuladas
        })
    
    # Salva o resultado em um arquivo JSON
    with open(output_json_path, "w", encoding="utf-8") as json_file:
        json.dump(questions, json_file, ensure_ascii=False, indent=4)

# Caminhos dos arquivos
pdf_file_path = "teste_enem_unzip/PROVAS E GABARITOS/LEITOR_TELA/ENEM_2023_P1_CAD_09_DIA_1_LARANJA_LEITOR_TELA_NVDA_CH.pdf"
output_image_dir = "imagem_pdf"
output_json_path = "enem_questions_corrected.json"

# Executa o script com o caminho do PDF
extract_questions_from_pdf(pdf_file_path, output_image_dir, output_json_path)
print(f"Arquivo JSON gerado em: {output_json_path}")
