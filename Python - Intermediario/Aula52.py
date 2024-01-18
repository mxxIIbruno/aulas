NOME, PRECO = 'nome', 'preco'


def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()


def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)


# def muda_preco_de_produtos(produto):
#     return {**produto, PRECO: aumentar_dez_porcento(produto[PRECO])} 


def filtrar_preco(produto):
    return produtos[PRECO] > 100


produtos = [
    {NOME: 'Produto 5', PRECO: 10.00},
    {NOME: 'Produto 1', PRECO: 22.32},
    {NOME: 'Produto 3', PRECO: 10.11},
    {NOME: 'Produto 2', PRECO: 105.87},
    {NOME: 'Produto 4', PRECO: 69.90},
]

# novos_produtos = [
#     p for p in produtos 
#     if p[PRECO] > 100
# ]

novos_produtos = filter(
    # lambda p: p[PRECO] >= 10,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
