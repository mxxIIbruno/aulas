frase = 'O Python é uma liguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

tamanho_da_frase = len(frase)
lista_de_palavras = []

for i in frase:
    if i not in lista_de_palavras:
        print(f'{i} apareceu {frase.count(i)}')
        lista_de_palavras.append(i)

print(lista_de_palavras)
