"""
    Sets - Conjuntos em Python (tipo set)
    Conjuntos são ensinados na matemática
    https://brasilescola.oul.com.br/matematica/conjunto.html
    Representados graficamente pelo diagrama de Venn
    Sets em Python são mutáveis, porem aceitam apenas
    tipos imtáveis como valor interno.

    Criando um set
    set(iterável) ou {1, 2, 3}

    Sets são eficientes para remover valores duplicados
    de iteráveis.
    - eles não tem índexes;
    - eles não garantem ordem;
    - eles são iteráveis (for, in, not in)

    Métodos úteis:
    add, update, clear, discard

    Operadores úteis:
    união | união (union) - Une
    intersecção & (intersection) - Itens presentes em ambos
    diferença - Itens presentes apenas no set da esquerda
    diferença simétrica ^- Itens que não estão em ambos
"""
from random import randint

var_set = set()

while len(var_set) < 100:
    var_set.add(randint(0, 1000))

print(len(var_set))
