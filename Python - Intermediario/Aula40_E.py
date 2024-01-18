from copy import deepcopy

NOME, PRECO = 'nome', 'preco'
"""
    Exercícios
    Aumente os preços dos produtos a seguir em 10%
    Gere novos_produtos por deep copy (cópia profunda)
"""
produtos = [
    {NOME: 'Produto 5', PRECO: 10.00},
    {NOME: 'Produto 1', PRECO: 22.32},
    {NOME: 'Produto 3', PRECO: 10.11},
    {NOME: 'Produto 4', PRECO: 105.87},
    {NOME: 'Produto 2', PRECO: 69.90},
]
novos_produtos = list()

for item in produtos:
    produto = deepcopy(item[NOME])
    preco = deepcopy(round(item[PRECO] + item[PRECO] * 0.1, 2))
    
    novos_produtos.append(
        {NOME: produto, PRECO: preco}
    )

# for item in range(len(produtos)):
#     print(
#         f'{produtos[item]}\n'
#         f'{novos_produtos[item]}\n'
#     )

"""
    Ordene os produtos por nome decrecente (do maior para o menor)
    Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""
produtos_ordenados_por_nome = []
lista_dos_nomes = sorted(
    [nome[NOME] for nome in novos_produtos],
    reverse=True
)

for nome in lista_dos_nomes:
    for item in novos_produtos:
        if nome in item[NOME]:
            produtos_ordenados_por_nome.append(deepcopy(
                {NOME: nome, PRECO: item[PRECO]}
            ))

# for item in range(len(novos_produtos)):
#     print(
#         f'{novos_produtos[item]}\n'
#         f'{produtos_ordenados_por_nome[item]}\n'
#     )

"""
    Ordene os produtos por preco crescente (do menor para o maior)
    Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
produtos_ordenados_por_preco = []
lista_dos_precos = sorted(
    [preco[PRECO] for preco in produtos_ordenados_por_nome]
)
for preco in lista_dos_precos:
    for item in novos_produtos:
        if preco == item[PRECO]:
            produtos_ordenados_por_preco.append(deepcopy(
                {NOME: item[NOME], PRECO: preco}
            ))

# for indice in range(len(novos_produtos)):
#     print(
#         f'{novos_produtos[indice]}\n'
#         f'{produtos_ordenados_por_preco[indice]}\n'
#     )
