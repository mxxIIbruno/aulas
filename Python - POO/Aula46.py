"""
    dataclasses - O que são dataclasses?
    O módulo dataclasses fornece um decorador e funções para criar métodos como
    __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
    usuário.
    Em resumo: dataclasses são syntax sugar para criar classes normais.
    Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
    doc: https://docs.python.org/3/library/dataclasses.html
"""
from dataclasses import asdict, astuple, dataclass


@dataclass
class Pessoa:
    nome: str
    sobrenome: str


if __name__ == '__main__':
    lista = Pessoa('A', 'Z')
    print(asdict(lista).keys())
    print(asdict(lista).values())
    print(asdict(lista).items())
    print(astuple(lista)[0])
    