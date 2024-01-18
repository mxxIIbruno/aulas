"""
    Lista em Python
    Tipo list - Mutável
    Suporta vários valores de qualquer tipo
    Conhecimentos reutilizáveis - índices e fatiamento
    Métodos úteis: 
        append, insert, pop, del, clear , extend, + 
    Create Read Update   Delete
    Criar, Ler, Alterar, Apagar = lista[i] (CRUD)
"""
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
ultimo_valor = lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop()  # Você pode remover por índice atravez do pop, Ex.: lista.pop(2), mas normalmente remove o ultimo valor!
print(lista, 'Removido,', ultimo_valor)
