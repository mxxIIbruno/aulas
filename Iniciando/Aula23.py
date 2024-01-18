"""
                Exercício
    Peça ao usuário para digitar seu nome
    Peça ao usuário para digitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Seu nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A ultima letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpe, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}!')
    print(f'Seu nome invertido é {nome[::-1]}!')
    print(f'Seu nome contem {nome.count(" ")} espaço(s)!')
    variavel = "".join(nome.split(" "))
    print(f'Seu nome contem {len(variavel)} letra(s) {variavel}')
    print(f'Seu nome começa com {nome[0]}!')
    variavel = nome.split()[0]
    print(f'Seu nome termina com {variavel[-1]}')
else:
    print('Deculpa, você deixou campos vazios!')
