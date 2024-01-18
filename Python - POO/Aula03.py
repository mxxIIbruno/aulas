# Métodos em instâcias de classes Python
class Carro:
    def __init__(self, nome) -> None:
        # self.nome = 'Fusca'  # Hard coded - É algo que foi escrito diretamente no código
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...\n')
    

fusca = Carro('Fusca')
fusca.acelerar()

celta = Carro('Celta')
celta.acelerar()
