"""
    Introdução às funções (def) em Python
    Funções são trechos de código usados para
    replicar determinada ação ao longo do seu código.
    Elas podem receber valores para parâmetros (argumentos)
    e retornar um valor específico.
    Por padão, fuções Python retornam None (nada)
"""

# def Print(a, b, c):
#     print('Várias1')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')


def imprimir(a='', b='', c=''):
    print(f'{a=}, {b=}, {c=}')

imprimir(10, 11, 12)
