"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
from os import system

LIMPAR = 'cls'
VAR_1 = '1'
VAR_2 = '2'

system(LIMPAR)

lista_compras = []
condition = True

while condition:
    if lista_compras:
        for i, v in lista_compras:
            print(f'Índice: {i}, Item: {v}')

    continuar = input('Você quer comprar? [1]Sim [2]Não -> ')
    system(LIMPAR)
    
    if continuar != VAR_1 and continuar != VAR_2:
        system(LIMPAR)
        print('Segue as instruções orientadas para efetuar a compra!')
        continue
    if continuar == VAR_2:
        system(LIMPAR)
        print('Volte sempre!')
        condition = not condition
        continue

    if lista_compras:
        system(LIMPAR)
        remover = input('Você quer remover um item? 1[Sim] [2]Não: ')
        if remover not in '12':
            system(LIMPAR)
            print('Segue as instruções orientadas para efetuar a compra!')
            continue
        if remover == VAR_1:
            indice = input('Qual índice deseja remover: ')
            if not indice.isdigit():
                system(LIMPAR)
                print('Segue as instruções orientadas para efetuar a compra!')
                continue
            if int(indice) > len(lista_compras):
                system(LIMPAR)
                print(f'Índice exede do tamanho da lista de compras: {len(lista_compras)}!')
                continue
            del lista_compras[int(indice)]
            continue
    
    lista_compras.append((len(lista_compras), input('Escolha um item: ')))

    
print('FIM!')
