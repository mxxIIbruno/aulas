from functools import reduce

NOME, PRECO = 'nome', 'preco'


def funcao_do_reduce(acumolador, produto):
    print('acumolador', acumolador)
    print('produto', produto)
    return produto[PRECO]
    

produtos = [
    {NOME: 'Produto 5', PRECO: 10.00},
    {NOME: 'Produto 1', PRECO: 22.32},
    {NOME: 'Produto 3', PRECO: 10.11},
    {NOME: 'Produto 2', PRECO: 105.87},
    {NOME: 'Produto 4', PRECO: 69.90},
]
total = reduce(
    lambda ac, p: ac + p[PRECO],
    produtos,
    0
)

# total = 0
# for p in produtos:
#     total += p[PRECO]

# print(total)
