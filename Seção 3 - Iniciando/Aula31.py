"""
    Faça um jogo para o usuário adivinhar qual a palavra secreta.
    - Você vai propor uma palavra secreta qualquer e vai dar a 
    possibilidade para o usuário digitar a penas uma letra.
    - Quando o usuário digitar uma letra, você vai conferir
    se a letra digitada está na palavra secreta.
        - Se a letra digitada estiver na palavra secreta; exiba a letra;
        - Se a letra digitada não estiver na palavra secreta; exiba *.
    Faça a contagem de tentativas do seu usuário.
"""
import string
import os

# Fazer apresentação do jogo da palavra secreta
text_line_1 = "jogo da palavra secreta".title()
print(f'\n{text_line_1:^65}\n')

# Pedir para o usuário uma letra
secret_word = 'Dinossauro'

condition = True
alphabet = string.ascii_lowercase
played_latters = ''
counter = 0

while condition:
    user_input = input('Digite uma letra: ')

    var_value_1 = user_input.lower()
    var_value_2 = secret_word.lower()
    var_value_3 = ''
   
    if len(user_input) > 1:
        print(f'Preciso de uma letra, você digitou -> "{user_input}"!')
        counter += 1
        continue
    if user_input not in alphabet:
        counter += 1
        print(f'"{user_input}" <- não é uma letra que existe no alfabeto!')
        continue

    played_latters += user_input
    counter += 1

    for letter in secret_word:
        if letter.lower() in played_latters:
            var_value_3 += letter
        else:
            var_value_3 += '*'
    
    if var_value_3 == secret_word:
        condition = not condition
        continue

    print(f'Qual é a palavra: {var_value_3}')


print('\nParabens você descobriu!')
print(f'A palavra é {secret_word}!')
print(f'O número de tentativas foi {counter}!')
print('Game-Over')

os.system('cls')
