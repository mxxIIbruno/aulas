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
for pessoa in range(len(bd_pessoas)):
    if pessoa % 2:
        print(f' x {bd_pessoas[pessoa]}')
        continue
    print(
        f'{bd_pessoas[pessoa]:>25}', end=''
    )
