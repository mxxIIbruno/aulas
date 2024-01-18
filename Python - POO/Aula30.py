"""
    __new__ e __init__ em classes Python
    __new__ é o método responsável por criar e
    retornar o novo objeto. Por isso, new recebe cls.
    __new__ ❗️DEVE retornar o novo objeto❗️
    __init__ é o método responsável por inicializar
    a instância. Por isso, init recebe self.
    __init__ ❗️NÃO DEVE retornar nada (None)❗️
    object é a super classe de uma classe
"""
class A:
    def __new__(cls, *args, **kwarg):
        # print('Antes de criar a instancia')
        instancia = super().__new__(cls)
        # print('Depois')
        # instancia.x = 123
        return instancia
        
    def __init__(self, x) -> None:
        self.x = x
        print('Sou o init')

    def __repr__(self) -> str:
        return f'A()'


a = A()
print(a.x)
