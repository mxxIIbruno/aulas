"""
    os.listdir para navegar em caminhos
    C:\\Users\\Mac II\\OneDrive\\Área de Trabalho\\Faculdade
"""
import os

caminho = os.path.join(
    'C:\\Users',
    'Mac II',
    'OneDrive',
    'Área de Trabalho',
    'Faculdade'
)
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for item in os.listdir(caminho_completo_pasta):
        print('\t' + item) 
