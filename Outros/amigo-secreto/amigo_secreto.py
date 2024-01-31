"""
    Codigo para gerar o amigo secreto do natal
"""
import random

import pessoas

# inserir pessoas na lista
bd_pessoas = pessoas.bd_list
random.shuffle(bd_pessoas)
bd_pessoas: list

# selecionar os amigos
print('\n\tLista do Amigo secreto oficial:')
for indice, pessoa in enumerate(bd_pessoas):
    if indice % 2:
        print(f' x {pessoa}')
        continue
    print(
        f'{pessoa:>25}', end=''
    )
