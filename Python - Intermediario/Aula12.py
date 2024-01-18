"""
    Métodos úteis dos dicionários em Python 
    len - quantas chaves
    keys - iterável com as chaves
    values - iterável com chaves e valores
    itens - iterável com chaves e valores
    setdefault - adicona valor se a chave não existe
    copy - retorne uma cópia rasa (shallow copy)
    get - obtém uma chave 
    pop - Apaga um item com a chave especificada (del)
    popitem - Apaga o último imte adicionado
    update - Atualiza um dicionário com outro
"""
dicionario_1 = {
    'nome': 'Bruno',
    'sobrenome': 'Monteiro'
}

dicionario_2 = {
    'meio': 'Silva',
    'sobrenome': 'Santos'
}

print(f'len(dicionario_1)                     -> {len(dicionario_1)}')
print(f'dicionario_1.keys()                   -> {dicionario_1.keys()}')
print(f'dicionario_1.values()                 -> {dicionario_1.values()}')
print(f'dicionario_1.items()                  -> {dicionario_1.items()}')
print(f'dicionario_1.setdefault()             -> {dicionario_1.setdefault("indigente")}')
print(f'dicionario_1.copy()                   -> {dicionario_1.copy()}')
print(f'dicionario_1.get("sobrenome")         -> {dicionario_1.get("sobrenome")}')
print(f'dicionario_1.pop()                    -> {dicionario_1.pop("nome")}')
print(f'dicionario_1.popitem()                -> {dicionario_1.popitem()}')
print(f'dicionario_1.update(dicionario_2)     -> {dicionario_1.update(dicionario_2)}')
