"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Bruno'
preco = 1000.95897643
variavel = '%s, preço é R$%.2f' % (nome, preco)

print(variavel)
print('O Heximadecimal de %d é %x' % (15, 15))
