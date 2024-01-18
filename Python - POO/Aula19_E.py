"""
    Exercício com classes
    1 - Crie uma classe Carro (Nome)
    2 - Crie uma classe Motor (Nome)
    3 - Crie uma classe Fabricante (Nome)
    4 - Faça uma ligação entre Carro tem Motor
    Obs.: Um motor pode ser de vários carros
    5 - Faça a ligação entre Carro e Fabricante
    Obs.: Um Fabricante pode fabricar vários carros
    Exiba o nome do carro, motor e fabricante na tela
"""
from itertools import product


class Carro:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.__motor = None
        self.__fabricante = None

    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, valor):
        self.__motor = valor

    @property
    def fabricante(self):
        return self.__fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self.__fabricante = valor

    def carro_tem(self):
        if self.motor is None:
            print(f'{self.nome} não tem motor!')
            return
        if self.fabricante is None:
            print(f'{self.nome} não tem fabricante!')
            return
        
        print(f'\n{self.nome} tem motor {self.motor}!')
        print(f'{self.nome} foi fabricado pela {self.fabricante}!\n')


class Motor:
    def __init__(self, nome) -> None:
        self.nome = nome


class Fabricante:
    def __init__(self, nome) -> None:
        self.nome = nome


carro_1 = Carro('Gol')
carro_2 = Carro('Uno')
carro_3 = Carro('Palio')

motor_1 = Motor('V8 Small Block')
motor_2 = Motor('HEMI')
motor_3 = Motor('V12')

fabricate_1 = Fabricante('Fiat')
fabricate_2 = Fabricante('Volkswagen')
fabricate_3 = Fabricante('Hyundai')

# carro_1.motor = motor_1.nome
# carro_1.carro_tem()

lista_carro = [carro_1, carro_2, carro_3]
lista_motor = [motor_1, motor_2, motor_3]
lista_fabricante = [fabricate_1, fabricate_2, fabricate_3]

# for carro in lista_carro:
#     for motor in lista_motor:
#         carro.motor = motor.nome
#         carro.carro_tem()
#     print()

for carro, motor, fabricante in product(lista_carro, lista_motor, lista_fabricante):
    carro.motor = motor
    carro.fabricante = fabricante
    
    carro.carro_tem()
