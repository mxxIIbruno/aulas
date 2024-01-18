import json

# pessoa = {
#     'nome': 'Bruno Santos',
#     'sobrenome': 'Silva',
#     'enderecos': [
#         {'rua': 'R1', 'numero': 32},
#         {'rua': 'R2', 'numero': 55}
#     ],
#     'altura': 1.8,
#     'numero_preferidos': (2, 4, 6, 8, 10),
#     'dev': True,
#     'nada': None 
# }

# with open('aula58.json', 'w', enconding='utf8) as arquivo:
#     json.dump(
#         pessoa, arquivo, 
#         ensure_ascii=False,
#         indent=2,
#     )

with open('aula58.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    # print(pessoa)
    # print(type(pessoa))
    print(pessoa['nome'])
