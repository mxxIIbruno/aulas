"""
    Valores padrão para parâmetros
    Ao definir uma função, os parâmetros podem
    ter valores padrão. Caso o valor não seja
    enviado para o parâmetro, o valor padrão 
    será usado.
    Refatorar: editar o seu código.
"""
def soma(x, y, z=None):
    if z is not None:
        result = x + y + z
        print(f'{x=} {y=} {z=} | x + y + z = {result}')
    else:
        result = x + y
        print(f'{x=} {y=} | x + y = {result}')


soma(z=2, y=3, x=4)
