import random 


def escolher_palavra():
    palavras = [
        'python', 'programacao', 'jogo', 'desenvolvimento', 'computador'
    ]
    return random.choice(palavras)


def exibir_forca(vidas):
    forca = [
        "  ____  ",
        " |    | ",
        f" |    {'O' if vidas < 6 else ' '}",
        # f" |   {'/' if vidas < 5 else ' '}{'' if vidas < 4 else '|'}{'\\' if vidas < 3 else ' '}",
        # f" |   {'/' if vidas < 2 else ' '} {'\\' if vidas < 1 else ' '}",
        " |       ",
        " |       ",
        "========="
    ]
    for linha in forca:
        print(linha)


def exibir_palavra_oculta(palavra, letras_corretas):
    palavra_mostrada = ''
    for letra in palavra:
        if letra in letras_corretas:
            palavra_mostrada += letra + ' '
        else:
            palavra_mostrada += '_ '
    return palavra_mostrada.strip()


def jogar_jogo_da_forca():
    palavra = escolher_palavra()
    letras_corretas = set()
    vidas = 6

    while vidas > 0:
        print('\nPalavra:', exibir_palavra_oculta(palavra, letras_corretas))
        exibir_forca(vidas)

        tentativa = input('Digite uma letra: ').lower()

        if tentativa in palavra:
            letras_corretas.add(tentativa)
            print('Correto!')
        else:
            print('Incorreto. Perdeu uma vida.')
            vidas -= 1

        if set(palavra) == letras_corretas:
            print('\nVocê perdeu. A palavra era:', palavra)
            break
    
    if vidas == 0:
        print('\nVocê perdeu. palavra era:', palavra)


if __name__ == '__main__':
    print('Bem-vindo ao Jogo da Forca!')
    jogar_jogo_da_forca()
