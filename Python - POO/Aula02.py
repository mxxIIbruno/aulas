"""
    class - Classes são moldes para criar novos objetos
    As classes geram novos objetos (instâncias) que
    podem ter seus próprios atributos e métodos.
    Os objetos gerados pela classe podem usar seus dados
    internos para realizar várias ações.
    Por convenção, usamos PascalCase para nomes classes.
"""
class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
    
    def revelar(self):
        print(self.nome, self.sobrenome, sep='\n')
        print()


p1 = Pessoa('Bruno', 'Santos')
p1.revelar()

p2 = Pessoa('Tereza', 'Monteiro')
p2.revelar()
