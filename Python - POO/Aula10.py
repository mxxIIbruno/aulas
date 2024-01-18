"""
    Método de classe + factories (fábricas)
    São médots onde "self" será cls, ou seja
    ao invés de receber a instância no primeiro
    parâmetro, recebebos a própria classe.
"""
class Pessoa:
    ano = 2023  #atributo de classe

    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)


p1 = Pessoa('Bruno', 'Santos')
p2 = Pessoa.criar_com_50_anos('Tereza')
p3 = Pessoa.criar_sem_nome(23)

print(vars(p1))
print(vars(p2))
print(vars(p3))
