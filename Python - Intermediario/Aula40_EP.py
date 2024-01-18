import copy

from Aula40_package import produtos, NOME, PRECO


def mostrar_lista(after, before):
    print(*after, sep='\n')
    print()
    print(*before, sep='\n')


"""
    Exercícios
    Aumente os preços dos produtos a seguir em 10%
    Gere novos_produtos por deep copy (cópia profunda)
"""
novos_produtos = [
    {**p, PRECO: round(p[PRECO] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]
# mostrar_lista(produtos, novos_produtos)

"""
    Ordene os produtos por nome decrecente (do maior para o menor)
    Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
"""
produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p[NOME],
    reverse=True
)
# mostrar_lista(produtos, produtos_ordenados_por_nome)

"""
    Ordene os produtos por preco crescente (do menor para o maior)
    Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
"""
produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p[PRECO]
)
# mostrar_lista(produtos, produtos_ordenados_por_preco)
