"""
    Texto para tirar o erro
    Gerou um erro
"""
from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

# print(caminho_arquivo.parent)

ideias = caminho_arquivo.parent.parent / 'ideias'
# print(ideias / 'arquivo.txt')

caminho_arquivo = Path.home() / 'Desktop' / 'arquivo.txt'
# arquivo.touch()
# print(arquivo)
# arquivo.write_text('Ola mundo')
# print(arquivo.read_text())
with caminho_arquivo.open('a+') as file:
    file.write('Uma linha\n')
    file.write('Duas linha\n')
