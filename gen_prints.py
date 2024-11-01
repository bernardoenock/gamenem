import fitz  # PyMuPDF
from pdf2image import convert_from_path
import json
import re
import os

# Diretório de saída para salvar as imagens dos enunciados
output_dir = "questao_prints"
os.makedirs(output_dir, exist_ok=True)

# Carrega o arquivo PDF
pdf_path = "PROVAS E GABARITOS 2021/ENEM_2021_P2_GAB_07_DIA_2_AZUL.pdf"
doc = fitz.open(pdf_path)

# Estrutura para armazenar os dados das questões
questoes_data = []

# Expressão regular para identificar o número da questão e alternativas
questao_re = re.compile(r'quest[ãa][oõ]?\s*[^\d]*(\d+)', re.IGNORECASE)
opcoes_re = re.compile(r'(A|B|C|D|E)\s+')

# Margens para o corte em pontos (ajuste conforme necessário)
margem_topo = 0    # 20 pontos acima do bloco do enunciado
margem_base = 2150    # > Altura
margem_esquerda = 0 # 20 pontos à esquerda
margem_direita = 1550  # > largura

# Função para salvar o recorte do enunciado da questão
def save_cropped_question_image(page, question_number, question_rect, last_option_rect, past_question_rect):
    # Converte a página PDF para imagem
    images = convert_from_path(pdf_path, first_page=page+1, last_page=page+1)

    print(f"---------------------------------------")
    print(f"margem_esquerda: {int(question_rect.x0)}")
    print(f"margem_direita: {int(question_rect.x1)}")
    print(f"---------------------------------------")
    print(f"margem_topo: {int(question_rect.y0)}")
    print(f"margem_base: {int(question_rect.y1)}")
    print(f"---------------------------------------")
    if (last_option_rect):
        print(f"----------ultima questão E-----------")
        print(f"margem_esquerda: {int(last_option_rect.x0)}")
        print(f"margem_direita: {int(last_option_rect.x1)}")
        print(f"---------------------------------------")
        print(f"margem_topo: {int(last_option_rect.y0)}")
        print(f"margem_base: {int(last_option_rect.y1)}")
        print(f"---------------------------------------")
    if(past_question_rect):
        print(f"past_question_rect-----> {past_question_rect}")
        print(f"---------------------------------------")
        print(f"margem_esquerda: {int(past_question_rect.x0)}")
        print(f"margem_direita: {int(past_question_rect.x1)}")
        print(f"---------------------------------------")
        print(f"margem_topo: {int(past_question_rect.y0)}")
        print(f"margem_base: {int(past_question_rect.y1)}")
        print(f"---------------------------------------")

# Questão: 93 Metade na direita
# ---------------------------------------
# margem_esquerda: 289
# margem_direita: 343
# ---------------------------------------
# margem_topo: 73
# margem_base: 88


# Questão: 96 Tela inteira
# ---------------------------------------
# margem_esquerda: 31
# margem_direita: 538 (Se é 538 é tela cheia)
# ---------------------------------------
# margem_topo: 73
# margem_base: 131



# quando a questão está na esquerda, margem_esquerda: 31
# quando a questão está na direita, margem_esquerda: 289

    fix_margem_esquerda = int(question_rect.x0)
    fix_margem_direita = int(question_rect.x1)
    fix_margem_topo = int(question_rect.y0)
    fix_margem_base = int(question_rect.y1)

    past_fix_margem_esquerda = 0
    past_fix_margem_direita = 0
    past_fix_margem_topo = 0
    past_fix_margem_base = 0
    if (past_question_rect):
        past_fix_margem_esquerda = int(past_question_rect.x0)
        past_fix_margem_direita = int(past_question_rect.x1)
        past_fix_margem_topo = int(past_question_rect.y0)
        past_fix_margem_base = int(past_question_rect.y1)


    if (fix_margem_direita <= 343):

        # Questões do lado esquerdo
        if (fix_margem_esquerda == 31):
            fix_margem_esquerda = int(question_rect.x0)


            if (fix_margem_topo == 563):
                fix_margem_topo = 1550
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 549):
                fix_margem_topo = 1500
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 520):
                if (past_fix_margem_base == 160):
                    fix_margem_topo = 1450
                    fix_margem_base = 2150
                    fix_margem_direita = 790
                else:
                    fix_margem_topo = 1500
                    fix_margem_base = 2150
                    fix_margem_direita = 790

            elif (fix_margem_topo == 486):
                fix_margem_topo = 1330
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 485):
                fix_margem_topo = 1330
                fix_margem_base = 2150
                fix_margem_direita = 790
            
            elif (fix_margem_topo == 473):
                fix_margem_topo = 1300
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 457):
                fix_margem_topo = 1250
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 445):
                fix_margem_topo = 1420
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 430):
                fix_margem_topo = 1200
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 381):
                fix_margem_topo = 1230
                fix_margem_base = 2090
                fix_margem_direita = 790

            elif (fix_margem_topo == 374):
                fix_margem_topo = 1040
                fix_margem_base = 2090
                fix_margem_direita = 790

            elif (fix_margem_topo == 357):
                fix_margem_topo = 980
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 306):
                if (past_fix_margem_base == 160):
                    fix_margem_topo = 1210
                    fix_margem_base = 2150
                    fix_margem_direita = 790
                else:
                    fix_margem_topo = 840
                    fix_margem_base = 2150
                    fix_margem_direita = 790
            
            elif (fix_margem_topo == 299):
                fix_margem_topo = 830
                fix_margem_base = 2150
                fix_margem_direita = 790
            
            elif (fix_margem_topo == 297):
                fix_margem_topo = 830
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 294):
                fix_margem_topo = 1020
                fix_margem_base = 2150
                fix_margem_direita = 790
            
            elif (fix_margem_topo == 287):
                fix_margem_topo = 800
                fix_margem_base = 1520
                fix_margem_direita = 1550

            elif (fix_margem_topo == 285):
                fix_margem_topo = 1150
                fix_margem_base = 2150
                fix_margem_direita = 790

            elif (fix_margem_topo == 239):
                fix_margem_topo = 650
                fix_margem_base = 1350
                fix_margem_direita = 790
            
            elif (fix_margem_topo == 180):
                fix_margem_topo = 790
                fix_margem_base = 1420
                fix_margem_direita = 790

            elif (fix_margem_topo == 73):
                fix_margem_topo = 200

                if (fix_margem_base == 88):
                    if (fix_margem_direita == 90):
                        if (past_fix_margem_base == 582):
                            fix_margem_base = 800
                            fix_margem_direita = 1550
                        elif (past_fix_margem_base == 515):
                            fix_margem_base = 2150
                            fix_margem_direita = 790
                        elif (past_fix_margem_base == 122):
                            fix_margem_base = 2000
                            fix_margem_direita = 790
                        else:
                            fix_margem_base = 1320
                            fix_margem_direita = 790
                    if (fix_margem_direita == 85):
                        if (past_fix_margem_base == 88):
                            fix_margem_base = 2150
                            fix_margem_direita = 790
                        else:
                            fix_margem_base = 1030
                            fix_margem_direita = 790
                    else:
                        fix_margem_base = 1350
                        fix_margem_direita = 790

                elif (fix_margem_base == 102):
                    if (past_fix_margem_base == 206):
                        fix_margem_base = 2150
                        fix_margem_direita = 790
                    else:
                        fix_margem_base = 1040
                        fix_margem_direita = 790   

                elif (fix_margem_base == 110):
                    fix_margem_base = 1040
                    fix_margem_direita = 790

                elif (fix_margem_base == 112):
                    fix_margem_base = 2150
                    fix_margem_direita = 790

                elif (fix_margem_base == 113):
                    fix_margem_base = 1530
                    fix_margem_direita = 790
                
                elif (fix_margem_base == 117):
                    fix_margem_base = 1200
                    fix_margem_direita = 790

                elif (fix_margem_base == 125):
                    fix_margem_base = 1250
                    fix_margem_direita = 790

                elif (fix_margem_base == 134):
                    fix_margem_base = 660
                    fix_margem_direita = 790

                elif (fix_margem_base == 160):
                    if (past_fix_margem_base == 245):
                         fix_margem_base = 1450
                         fix_margem_direita = 790
                    else:
                        fix_margem_base = 1220
                        fix_margem_direita = 790

                elif (fix_margem_base == 172):
                    fix_margem_base = 2150
                    fix_margem_direita = 790
                
                elif (fix_margem_base == 175):
                    fix_margem_base = 2150
                    fix_margem_direita = 790

                elif (fix_margem_base == 178):
                    fix_margem_base = 1570
                    fix_margem_direita = 790
                
                elif (fix_margem_base == 179):
                    fix_margem_base = 800
                    fix_margem_direita = 790

                elif (fix_margem_base == 183):
                    if (past_fix_margem_topo == 298):
                        fix_margem_base = 840
                        fix_margem_direita = 790
                    elif (past_fix_margem_base == 330):
                        fix_margem_base = 2150
                        fix_margem_direita = 790
                    else:
                        fix_margem_base = 1000
                        fix_margem_direita = 790

                elif (fix_margem_base == 195):
                    fix_margem_base = 850
                    fix_margem_direita = 790

                elif (fix_margem_base == 204):
                    fix_margem_base = 2150
                    fix_margem_direita = 790

                elif (fix_margem_base == 218):
                    fix_margem_base = 830
                    fix_margem_direita = 790

                elif (fix_margem_base == 245):
                    fix_margem_base = 2150 
                    fix_margem_direita = 790             

                elif (fix_margem_base == 272):
                    fix_margem_base = 1150
                    fix_margem_direita = 790

                elif (fix_margem_base == 331):
                    fix_margem_base = 1230
                    fix_margem_direita = 790
                            
                else:
                    fix_margem_base = 1000
            else:
                fix_margem_direita = 790

        # Questões do lado direito
        elif (fix_margem_esquerda == 289):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            # fix_margem_topo = 0

            if (fix_margem_topo == 534):
                fix_margem_topo = 1480
                fix_margem_base = 2150

            elif (fix_margem_topo == 298):
                fix_margem_topo = 820
                fix_margem_base = 1490
            
            elif (fix_margem_topo == 218):
                fix_margem_topo = 600
                fix_margem_base = 2150

            elif (fix_margem_topo == 73):
                if (fix_margem_base == 88):
                    if (past_fix_margem_base == 88):
                        fix_margem_topo = 200
                        fix_margem_base = 2150
                    else:
                        fix_margem_topo = 200
                        fix_margem_base = 2150
                else:
                    fix_margem_topo = 200
                    fix_margem_base = fix_margem_base * 9.5

    elif (fix_margem_direita > 343):

        fix_margem_direita = 1550

        if (fix_margem_topo == 73):

            if (fix_margem_esquerda == 289):
                
                if (fix_margem_base == 525 and last_option_rect == None):
                    fix_margem_topo = 200
                    fix_margem_base = 890
                    fix_margem_esquerda = 790
                
                elif (fix_margem_base == 525):
                    fix_margem_topo = 880
                    fix_margem_base = 2100
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 449):
                    fix_margem_topo = 200
                    fix_margem_base = 2100
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 376):
                    fix_margem_topo = 600
                    fix_margem_base = 1300
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 313):
                    fix_margem_topo = 600
                    fix_margem_base = 1300
                    fix_margem_esquerda = 790
                
                elif (fix_margem_base == 245):
                    fix_margem_topo = 200
                    fix_margem_base = 1400
                    fix_margem_esquerda = 790
                
                elif (fix_margem_base == 190):
                    fix_margem_topo = 200
                    fix_margem_base = 1360
                    fix_margem_esquerda = 790
                
                elif (fix_margem_base == 169 and last_option_rect == None):
                    fix_margem_topo = 200
                    fix_margem_base = 1300
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 169):
                    fix_margem_topo = 200
                    fix_margem_base = 2050
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 134):
                    fix_margem_topo = 200
                    fix_margem_base = 2150
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 137):
                    fix_margem_topo = 200
                    fix_margem_base = 840
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 122):
                    fix_margem_topo = 200
                    fix_margem_base = 2050
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 100):
                    fix_margem_topo = 200
                    fix_margem_base = 2050
                    fix_margem_esquerda = 790

                elif (fix_margem_base == 88):
                    if (past_fix_margem_base == 88):
                        fix_margem_topo = 200
                        fix_margem_base = 880
                        fix_margem_esquerda = 790
                    else:
                        fix_margem_topo = 200
                        fix_margem_base = 920
                        fix_margem_esquerda = 790

                else:
                    fix_margem_topo = 200
                    fix_margem_base = 1300
                    fix_margem_esquerda = 790
            elif (fix_margem_esquerda == 31):

                if (fix_margem_base == 411):
                    fix_margem_topo = 200
                    fix_margem_base = 1040

                elif (fix_margem_base == 137):
                    if (past_fix_margem_base == 666):
                        fix_margem_topo = 200
                        fix_margem_base = 680
                    else:
                        fix_margem_topo = 200
                        fix_margem_base = 1040

                elif (fix_margem_base == 131):
                    fix_margem_topo = 200
                    fix_margem_base = 850

                else:
                    fix_margem_topo = 200
                    fix_margem_base = 700

            else:
                fix_margem_topo = 200
                fix_margem_base = 850

        elif (fix_margem_topo == 156):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 830
            fix_margem_base = 2150
        
        elif (fix_margem_topo == 188):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 520
            fix_margem_base = 1420
        
        elif (fix_margem_topo == 209):
            if (past_fix_margem_base == 624):
                fix_margem_esquerda = 790
                fix_margem_direita = 1550
                fix_margem_topo = 590
                fix_margem_base = 1900
            else:
                fix_margem_esquerda = 790
                fix_margem_direita = 1550
                fix_margem_topo = 590
                fix_margem_base = 1700

        elif (fix_margem_topo == 248):
            fix_margem_topo = 670
            fix_margem_base = 1100
            fix_margem_esquerda = 0
            fix_margem_direita = 1550
        
        elif (fix_margem_topo == 264):
            fix_margem_topo = 700
            fix_margem_base = 2150
            fix_margem_esquerda = 790
            fix_margem_direita = 1550

        elif (fix_margem_topo == 272):
            fix_margem_topo = 750
            fix_margem_base = 1400
            fix_margem_esquerda = 790
            fix_margem_direita = 1550

        elif (fix_margem_topo == 289):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 800
            fix_margem_base = 2150

        elif (fix_margem_topo == 298):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 800
            fix_margem_base = 2150

        elif (fix_margem_topo == 303):
            fix_margem_topo = 850
            fix_margem_base = 1420

        elif (fix_margem_topo == 316):
            fix_margem_esquerda = 790
            fix_margem_topo = 880
            fix_margem_base = 2150

        elif (fix_margem_topo == 333):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 920
            fix_margem_base = 2150

        elif (fix_margem_topo == 371):
            fix_margem_topo = 1030
            fix_margem_base = 2150

        elif (fix_margem_topo == 374):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1080
            fix_margem_base = 2150

        elif (fix_margem_topo == 376):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1300
            fix_margem_base = 2150

        elif (fix_margem_topo == 402):
            fix_margem_esquerda = 0
            fix_margem_direita = 1550
            fix_margem_topo = 1100
            fix_margem_base = 2080

        elif (fix_margem_topo == 420):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1150
            fix_margem_base = 2080

        elif (fix_margem_topo == 465):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1290
            fix_margem_base = 2080
        
        elif (fix_margem_topo == 489):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1350
            fix_margem_base = 2080

        elif (fix_margem_topo == 501):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1400
            fix_margem_base = 2080

        elif (fix_margem_topo == 511):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1420
            fix_margem_base = 2100

        elif (fix_margem_topo == 514):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1420
            fix_margem_base = 2100

        elif (fix_margem_topo == 515):
            fix_margem_topo = 1420
            fix_margem_base = 2100

        elif (fix_margem_topo == 518):
            fix_margem_esquerda = 790
            fix_margem_direita = 1550
            fix_margem_topo = 1420
            fix_margem_base = 2100
        else:
            fix_margem_topo = 0
            fix_margem_base = 2150
    else:  
        fix_margem_topo = 0
        fix_margem_base = 2150
        fix_margem_esquerda = 0
        fix_margem_direita = 1550

    # Define uma nova área de recorte com as margens ajustadas
    cropped_rect = fitz.Rect(
        fix_margem_esquerda,
        fix_margem_topo,
        fix_margem_direita,
        fix_margem_base
    )

    # Recorta a imagem com as novas margens
    cropped_image = images[0].crop((
        cropped_rect.x0,
        cropped_rect.y0,
        cropped_rect.x1,
        cropped_rect.y1
    ))

    # Define o caminho da imagem recortada
    image_path = os.path.join(output_dir, f"QUESTAO_{question_number:02d}.png")
    cropped_image.save(image_path, "PNG")
    return image_path

# Inicializa uma lista para armazenar os dados das questões
questoes_data = []

last_option_rect = None
past_question_rect = None  # Variável para armazenar o rect da questão anterior

# Loop pelas páginas para identificar e extrair as questões
for page_num in range(doc.page_count):
    page = doc[page_num]
    blocks = page.get_text("blocks")  # Extrai blocos de texto com coordenadas

    print(f'\n--- Página {page_num} ---\n')  # Adiciona um separador para cada página

    # Processa cada bloco de texto na página
    for idx, block in enumerate(blocks):
        block_text = block[4]

        # Procura por todas as ocorrências de "QUESTÃO xx" dentro do bloco
        questoes_encontradas = list(questao_re.finditer(block_text))

        # Verifica se há mais de uma questão no mesmo bloco
        if len(questoes_encontradas) > 1:
            for i, questao_match in enumerate(questoes_encontradas):
                question_number = int(questao_match.group(1))

                # Define o índice inicial e final para extrair o texto da questão
                start_idx = questao_match.start()
                end_idx = questoes_encontradas[i + 1].start() if i + 1 < len(questoes_encontradas) else len(block_text)
                
                # Extrai o texto da questão específica
                questao_texto = block_text[start_idx:end_idx]

                # Define o retângulo (bounding box) do enunciado da questão atual
                question_rect = fitz.Rect(block[:4])

                print(f'** Questão {question_number} detectada no bloco {idx} da página {page_num} **')

                # Salva a imagem recortada do enunciado da questão com margens ajustadas
                image_path = save_cropped_question_image(page_num, question_number, question_rect, last_option_rect, past_question_rect)

                # Atualiza o retângulo da questão anterior
                past_question_rect = question_rect

                # Extrai as alternativas (A até E) para a questão
                opcoes = {}
                opcoes_matches = list(opcoes_re.finditer(questao_texto))
                if opcoes_matches:
                    for idx, opcao_match in enumerate(opcoes_matches):
                        opcao_letter = opcao_match.group(1)
                        # Extrai o texto da opção usando o intervalo entre as correspondências
                        start_idx = opcao_match.end()
                        end_idx = opcoes_matches[idx + 1].start() if idx + 1 < len(opcoes_matches) else len(questao_texto)
                        opcao_text = questao_texto[start_idx:end_idx].strip()
                        opcoes[opcao_letter] = opcao_text

                    # Verifica se a última alternativa é "E" e atualiza last_option_rect
                    if opcao_letter == 'E':
                        last_option_rect = fitz.Rect(block[:4])

                # Adiciona a questão ao JSON
                questoes_data.append({
                    "title": f"QUESTÃO {question_number}",
                    "options": opcoes,
                    "image_path": image_path
                })
        else:
            # Caso contrário, processa o bloco normalmente
            questao_match = questao_re.search(block_text)
            if questao_match:
                question_number = int(questao_match.group(1))

                print(f"Questão: {question_number}")
                
                # Define o retângulo (bounding box) do enunciado da questão atual
                question_rect = fitz.Rect(block[:4])

                # Salva a imagem recortada do enunciado da questão com margens ajustadas
                image_path = save_cropped_question_image(page_num, question_number, question_rect, last_option_rect, past_question_rect)
                
                # Atualiza o retângulo da questão anterior
                past_question_rect = question_rect

                # Extrai as alternativas (A até E) para a questão
                opcoes = {}
                opcoes_matches = list(opcoes_re.finditer(block_text))
                if opcoes_matches:
                    for idx, opcao_match in enumerate(opcoes_matches):
                        opcao_letter = opcao_match.group(1)
                        # Extrai o texto da opção usando o intervalo entre as correspondências
                        start_idx = opcao_match.end()
                        end_idx = opcoes_matches[idx + 1].start() if idx + 1 < len(opcoes_matches) else len(block_text)
                        opcao_text = block_text[start_idx:end_idx].strip()
                        opcoes[opcao_letter] = opcao_text

                    # Verifica se a última alternativa é "E" e atualiza last_option_rect
                    if opcao_letter == 'E':
                        last_option_rect = fitz.Rect(block[:4])
                else:
                    last_option_rect = None  # Redefine caso não encontre alternativas

                # Adiciona a questão ao JSON
                questoes_data.append({
                    "title": f"QUESTÃO {question_number}",
                    "options": opcoes,
                    "image_path": image_path
                })

# Salva os dados no formato JSON
json_path = "questoes_data.json"
with open(json_path, "w", encoding="utf-8") as json_file:
    json.dump(questoes_data, json_file, ensure_ascii=False, indent=4)

print(f"Process completed! Data saved to {json_path} and images saved in {output_dir}")
