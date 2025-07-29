import os
import json

folder = "microdados_enem_2023/PROVAS_E_GABARITOS"
pdfs = [f for f in os.listdir(folder) if f.endswith(".pdf")]

with open(os.path.join(folder, "pdfs.json"), "w") as f:
    json.dump(pdfs, f)