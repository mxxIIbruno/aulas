"""
    Exercício
    Crie uma função que encotra o primeiro duplicado considerando o segundo
    número como a duplicação. Retorne a duplicação considerada.
    Requisitos:
        A ordem do numero duplicado é considerada a partir da segunda
        ocorrência do número, ou seja, o número duplicado em si.
        Exemplo:
            [1, 2, 3, 3, 2, 1] -> 1, 2 e 3 são duplicados (retorne 3)
            [1, 2, 3, 4, 5, 6] -> Retorne -1 (não tem duplicados)
        Se não encontrar duplicados na lista, retorne -1
"""
def retornar_primeiro_duplicado(*args):
    var_funcao_a = list(*args)
    var_set = set()

    for elemento in var_funcao_a:
        if elemento in var_set:
            return elemento
        var_set.add(elemento)
    return -1


def sep_lista(*args):
    var_lista_b = list(*args)
    var_dicionario = dict()

    for indice in var_lista_b:
        var_dicionario_for = dict()
        var_dicionario_for[str(indice)] = retornar_primeiro_duplicado(indice)
        var_dicionario.update(var_dicionario_for.copy())

    for indice in var_dicionario.items():
        if indice[1] < 0:
            print(f'O índice {indice[0]} não possui número repetido!')
        else:
            print(f'O índice {indice[0]} aparece {indice[1]} como primeiro número duplicado!')


lista_de_listas_de_inteiros = [
    [1,2,3,4,5,6,7,8,9,10],
    [9,1,8,9,9,7,2,1,6,8],
    [1,3,2,2,8,6,5,9,6,7],
    [3,8,2,8,6,7,7,3,1,9],
    [4,8,8,8,5,1,10,3,1,7],
    [1,3,7,2,2,1,5,1,9,9],
    [10,2,2,1,3,5,10,5,10,1],
    [1,6,1,5,1,1,1,4,7,3],
    [1,3,7,1,10,5,9,2,5,7],
    [4,7,6,5,2,9,2,1,2,1],
    [5,3,1,8,5,7,1,8,8,7],
    [10,9,8,7,6,5,4,3,2,1]
]

sep_lista(lista_de_listas_de_inteiros)
