from os import system
from string import ascii_lowercase

def limpar():
    system('cls')


def titulo():
    limpar()
    texto_1 = 'Palavra Secreta'
    print(f'\n{texto_1:^50}\n')


palavra_secreta = None
letras_jogador = ''
condicao = True
gameOver = True
count = 0

while gameOver:
    if condicao:
        titulo()
        palavra_secreta = input('Digite a palavra secreta: ')
        condicao = not condicao

    titulo()

    var_palavra_secreta = ''
    for letra in palavra_secreta:
        if letra.lower() in letras_jogador:
            var_palavra_secreta += letra
        elif letra == ' ' or letra == '-':
            var_palavra_secreta += letra
        else:
            var_palavra_secreta += '_'
    
    if var_palavra_secreta == palavra_secreta:
        titulo()
        print('Parabens você descobriu!')
        print(f'A palavra secreta é: {palavra_secreta}')
        print(f'Você fez {count}x de tentativas!')
        print('Game-Over\n')
        contiuar = input('Quer continuar? [S]im: ').upper()
        if contiuar == 'S':
            condicao = not condicao
            letras_jogador = ''
            count = 0
        else:
            gameOver = not gameOver
        continue

    print(f'Qual é?                     -> {var_palavra_secreta}')

    letra_usuario = input('Digite uma letra: ').lower()
    count += 1
    
    if len(letra_usuario) > 1:
        titulo()
        print(f'Digite uma letra, você digitou -> "{letra_usuario}"!')
        continue

    if letra_usuario not in ascii_lowercase + 'ç' and letra_usuario not in palavra_secreta:
        titulo()
        print(f'Digite uma letra do alfabeto, você digitou -> "{letra_usuario}"!')
        continue

    if letra_usuario in palavra_secreta.lower():
        letras_jogador += letra_usuario
    
print()
