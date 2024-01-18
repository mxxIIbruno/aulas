def imprimir(message):
    print(f'{message=}, {falsy(message)}')


def falsy(valor):
    return 'falsy' if not valor else 'truthy'


lista = list()
dicionario = dict()
setter = set()

imprimir(lista)
imprimir(dicionario)
imprimir(setter)
