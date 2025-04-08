import os
import requests
from bs4 import BeautifulSoup

def baixar_csv_anac(pagina_index_url: str, caminho_salvar: str):
    response = requests.get(pagina_index_url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')

    link_csv = None
    for link in soup.find_all('a'):
        href = link.get('href')
        if href and href.lower().endswith("dados_estatisticos.csv"):
            link_csv = href
            break

    if not link_csv:
        raise Exception("Arquivo CSV não encontrado na página!")

    if not pagina_index_url.endswith("/"):
        pagina_index_url += "/"
    url_csv = pagina_index_url + link_csv

    print(f"[INFO] Baixando arquivo de: {url_csv}")
    print(f"[DEBUG] Salvando em: {caminho_salvar}")

    os.makedirs(os.path.dirname(caminho_salvar), exist_ok=True)

    csv_response = requests.get(url_csv, stream=True)
    csv_response.raise_for_status()

    with open(caminho_salvar, "wb") as f:
        for chunk in csv_response.iter_content(chunk_size=1048576):  # 1MB
            if chunk:
                f.write(chunk)

    print(f"[SUCESSO] CSV salvo em {caminho_salvar}")
