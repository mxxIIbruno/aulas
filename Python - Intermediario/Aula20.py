# from os import system
# from time import sleep

# bruno = 'bruno'
# lista = list(bruno)

# count = 0

# while count < 10:
#     for i in lista:
#         system('cls')
#         indice = lista.index(i)
#         letra = lista[indice].upper()

#         messagem = ''.join(lista).replace(i, letra)
#         print(messagem)
        
#         sleep(0.25)
    
#     for i in range(3):
#         system('cls')
#         sleep(0.5)
#         print(''.join(lista).upper())
#         sleep(0.5)
#         system('cls')

#     count += 1
a, b = 1, 2
a, b = b, a
# print(a, b)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza'
}
dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

pessoas_completa = {**pessoa, **dados_pessoa}

# (a1, a2), b = pessoa.items()
# print(a1, a2)
# print(b)

def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4
}

mostro_argumentos_nomeados(**configuracoes)