import string
from random import randint

palavra = 'Bruno'
palavra_criptografada = ''

alpha = string.ascii_letters
chave = randint(1, len(alpha))

for letra in palavra:
    indice = alpha.index(letra)
    nova_letra = alpha[(indice + chave) % len(alpha)]
    palavra_criptografada += nova_letra

print(f'Palavra: {palavra}\nCriptografada: {palavra_criptografada}\nChave: {chave}')
