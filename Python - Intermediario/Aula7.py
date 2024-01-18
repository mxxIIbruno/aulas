import os

os.system('cls')

lista_1 = (1, 2, 3)
lista_2 = (4, 5, 6)

lista_3 = [sum((x, y)) for x in lista_1 for y in lista_2]
print(lista_3)
