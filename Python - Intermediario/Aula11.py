"""
    Exercícios

    Crie funções que duplicam, triplicam e quadriplicam
    número recebido como parâmetro
"""
def duplicar(num):
    return num * 2

def triplicar(num):
    return num * 3

def quadriplicar(num):
    return num * 4

def mostrar_resultado(func, arg):
    return func(arg)

var_a = mostrar_resultado(duplicar, 5)
var_b = mostrar_resultado(triplicar, 5)
var_c = mostrar_resultado(quadriplicar, 5)

print( \
    f'Duplicar: {var_a=}\n \
    Triplicar: {var_b=}\n \
    Quadriplicar: {var_c=}')
