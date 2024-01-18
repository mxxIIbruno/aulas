from functools import partial
from types import GeneratorType

NOME, PRECO = 'nome', 'preco'


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


def muda_preco_de_produtos(produto):
    return {**produto, PRECO: aumentar_dez_porcento(produto[PRECO])} 

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

produtos = [
    {NOME: 'Produto 5', PRECO: 10.00},
    {NOME: 'Produto 1', PRECO: 22.32},
    {NOME: 'Produto 3', PRECO: 10.11},
    {NOME: 'Produto 2', PRECO: 105.87},
    {NOME: 'Produto 4', PRECO: 69.90},
]

# novos_produtos = [
#     {**p, PRECO: aumentar_dez_porcento(p[PRECO])} 
#     for p in produtos
# ]

novos_produtos = map(
    muda_preco_de_produtos,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)

# print(novos_produtos)

# print(hasattr(novos_produtos, '__iter__'))
# print(hasattr(novos_produtos, '__next__'))

# print(isinstance(novos_produtos, GeneratorType))

print(
    list(map(
        lambda x: x * 3,
        [1, 2, 3, 4]
    ))
)
