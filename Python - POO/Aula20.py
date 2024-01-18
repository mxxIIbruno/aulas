"""
    Herança simples - Relações entre classes
    Associação - usa, Agregação - tem
    Composição - É dono de, Herança - É tem

    Herança ou Composição

    Classe principal (Pessoa)
        -> super class, base class, parent class
    Classes filhas (CLiente)
        -> sub class, child class, derived class
"""
class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(
            self.nome , self.sobrenome,
            self.__class__.__name__
        )


class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...


c1 = Cliente('Bruno', 'Santos')
a1 = Aluno('Suzana', 'Vieira')

c1.falar_nome_classe()
a1.falar_nome_classe()
