from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, idade):
        super().__init__()
        self.__nome = nome
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    
    @property
    def idade(self):
        return self.__idade
    

class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

