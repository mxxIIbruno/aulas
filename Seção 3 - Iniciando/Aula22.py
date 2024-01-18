"""
    Formatação básica de strings
    s - string
    d - int 
    f - float
    .<número de dígitos>f
    x ou X Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esquerda 
    < - Direita
    ^ - Centro
    = - Força o número aparecer antes dos zeros
    Sinal - + ou -
    Ex.: 0>-100,.1f
    Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')

print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')

print(f'{1000.456123879:0=+10,.2f}')
print(f'O hexadecimal de 1500 é {1500:08X}')

print(f'{variavel!r}')
