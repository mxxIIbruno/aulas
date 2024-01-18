"""
    Argumentos nomeados e não nomeados em funções Python
    Argumentos nomeado tem nome com sinal de igual
    Argumento não nomeado recebe apenas o argumento (valor)
"""
def soma(x=0, y=0, z=0):
    result = x + y - z
    print(f'{x=} {y=} {z=} | x + y - z = {result}')


soma(2, 4, 9)
