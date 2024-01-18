"""
    Método especial __call__
    callable é algo que pode ser executado com parêntes
    Em classes normais, __call__ faz a instâcia de uma
    classe "callable".
"""
class CallMe:
    def __init__(self, phone) -> None:
        self.phone = phone

    def __call__(self, nome):
        print(nome, 'Chamando', self.phone)
        return 12345


call = CallMe('123546798132')
retorno = call('Bruno')

print(retorno)
