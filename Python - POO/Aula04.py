"""
    Métodos em instâcias de classes Python
    Classe - Molde (geralmente sem dados)
    Instâcia da class (objeto) - Tem os dados
    Uma classe pode gerar várias instâncias.
    Na classe o self é a própria instâcia.
"""
class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')
    

fusca = Carro('Fusca')
Carro.acelerar(fusca)
# print(fusca.nome)
# fusca.acelerar()

celta = Carro('Celta')
Carro.acelerar(celta)
# print(celta.nome)
# celta.acelerar()
