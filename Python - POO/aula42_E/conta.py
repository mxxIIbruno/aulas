from abc import ABC, abstractmethod
from random import randint


class Conta(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__agencia = str(randint(1, 999))
        self.__conta = f'{randint(10000, 999999)}-{randint(0, 99)}'
        self._saldo = float()
    
    @property
    def agencia(self):
        return self.__agencia
    
    @property
    def conta(self, valor):
        return self.__conta
    
    @property
    def saldo(self):
        return self._saldo
    
    def depositar(self, valor):
        self._saldo += valor
        print('\nDeposito realizado com sucesso!\n')

    @abstractmethod
    def sacar(self, valor): ...

    def dados(self):
        class_name = self.__class__.__name__
        print('\nAgencia:', self.__agencia)
        print('Tipo de Conta:', class_name)
        print('Conta:', self.__conta)
        print(f'Salto atual: R${self.saldo:,.2f}\n')


class ContaCorrente(Conta):
    __limite_extra = -500
    
    def sacar(self, valor: int | float):
        if self._saldo - valor <= self.__limite_extra:
            print(f'\nSaldo insuficiente! Limite extra: R${self.__limite_extra:,.2f}')
            print(f'Saldo atual: R${self._saldo:,.2f}')
            print(f'Valor desejado: R${valor:,.2f}\n')
            return
        
        self._saldo -= valor
        print('\nSaque realizado com sucesso!\n')
        
        return super().sacar(valor)


class ContaPoupanca(Conta):
    def sacar(self, valor: int | float):
        if self.saldo - valor <= 0:
            print('Saldo insuficiente para sacar!')
            print(f'Saldo atual: R${self.saldo:,.2f}')
            print(f'Valor desejado: R${valor:,.2f}')
            return
        
        self._saldo -= valor
        print('\nSaque realizado com sucesso!\n')

        return super().sacar(valor)
