"""
    Exercício - Salve sua classe em JSON
    Salve os dados da sua classe em JSON
    e depois crie novamente as instâcias
    da classe com os dados salvos
    Faça em arquivos separados.
"""
import os
import json

CAMINHO = 'aula09.json'
ENCODING = 'utf8'

caminho_do_arquivo = 'C:\\Users\\Mac II\\PycharmProjects\\pythonProject1\\IniciarCurso\\Seção 3\\POO\\' + CAMINHO


class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome


if os.path.exists(caminho_do_arquivo):
    with open(CAMINHO, 'r', encoding=ENCODING) as arquivo:
        dados = json.load(arquivo)
        pessoa_2 = Pessoa(**dados)
        print(f'{pessoa_2.nome=}')
        print(f'{pessoa_2.sobrenome=}')
else:
    dado_p1 = Pessoa('Bruno', 'Santos')
    salvar_dicionario = dado_p1.__dict__

    with open(CAMINHO, 'w', encoding=ENCODING) as arquivo:
        json.dump(salvar_dicionario, arquivo, indent=2)
    print('Criei dados agora')
