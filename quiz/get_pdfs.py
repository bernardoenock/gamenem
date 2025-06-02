import requests
import zipfile
import os
from tqdm import tqdm  # Para a barra de progresso

# URL do arquivo zip para download
url = "https://download.inep.gov.br/microdados/microdados_enem_2022.zip"
# Nome do arquivo zip a ser salvo localmente
zip_file_name = "microdados_enem_2022.zip"
# Diretório onde os PDFs serão salvos
output_folder = "provas_pdfs"
# Palavra-chave para filtrar os arquivos desejados
keyword = "LARANJA"

# 1. Fazer o download do arquivo zip com barra de progresso
response = requests.get(url, stream=True)
file_size = int(response.headers.get('content-length', 0))
chunk_size = 8192

if response.status_code == 200:
    with open(zip_file_name, "wb") as file, tqdm(
        desc="Baixando o arquivo",
        total=file_size,
        unit='B',
        unit_scale=True,
        unit_divisor=1024,
    ) as progress_bar:
        for chunk in response.iter_content(chunk_size=chunk_size):
            if chunk:
                file.write(chunk)
                progress_bar.update(len(chunk))
    print("\nDownload concluído com sucesso! 📥")
else:
    print("Falha no download. Código de status:", response.status_code)
    exit()

# 2. Verificar se o arquivo zip foi baixado
if not os.path.exists(zip_file_name):
    print(f"Erro: O arquivo {zip_file_name} não foi encontrado após o download.")
    exit()

# 3. Extrair apenas os PDFs com 'LEITOR_TELA' no nome para a pasta de saída
with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
    # Listar todos os arquivos no zip
    all_files = zip_ref.namelist()
    print("Arquivos encontrados no zip:")
    for f in all_files:
        print(f)

    # Filtrar os arquivos PDF que contêm 'LEITOR_TELA' no nome
    pdf_files = [f for f in all_files 
                 if keyword in f and f.endswith(".pdf")]

    # Criar a pasta de saída se ela não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print(f"\nExtraindo {len(pdf_files)} arquivos PDF para '{output_folder}'... 📂")
    for file in tqdm(pdf_files, desc="Extraindo PDFs"):
        # Extrair cada PDF diretamente para a pasta de saída
        destination_path = os.path.join(output_folder, os.path.basename(file))
        with open(destination_path, "wb") as pdf_out:
            pdf_out.write(zip_ref.read(file))

# 4. Remover o arquivo zip e a pasta 'microdados_enem_2023' após a extração
if os.path.exists(zip_file_name):
    os.remove(zip_file_name)
    print("\nArquivo zip excluído. 🗑️")

print("Processo completo! PDFs com 'LEITOR_TELA' estão na pasta 'provas_pdfs'. 📂")
