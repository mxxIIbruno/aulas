# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'Aula19.json'
CAMINHO_ABSOLUTP_ARQUIVO = os.path.abspath(
    os.path.join(os.path.dirname(__file__), NOME_ARQUIVO))

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None
}

with open(CAMINHO_ABSOLUTP_ARQUIVO, 'w', encoding='utf8') as arquivos:
    json.dump(filme, arquivos, ensure_ascii=False, indent=2)

with open(CAMINHO_ABSOLUTP_ARQUIVO, 'r', encoding='utf8') as arquivos:
    filme_do_json = json.load(arquivos)
    print(filme)
