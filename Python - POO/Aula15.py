"""
    Emcapsulamento (modificadores de acesso: public, protected, private)
    Python NÃO TEM modificadores de acesso
    Mas podemos seguir as seguintes convenções
        (sem underline) = public
            pode ser usado em qualquer lugar
        _ (um underline) = protected
            não DEVE ser usado fora da classe
            ou suas subclasses.
        __ (dois underlines) = private
            "name mangling" (desfiguração de nome) em Python
            só DEVE ser usado na classe que foi declarado.
"""
class Foo:
    def __init__(self) -> None:
        self.public = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        self._metodo_protected()
        print(self._protected)
        return 'metodo_publico'

    def _metodo_protected(self):
        print('_metodo_protected')
        return '_metodo_protected'
    
    def __metodo_private(self):
        print('__metodo_private')
        return '__metodo_private'


f = Foo()
print(f.metodo_publico())
# print(f._Foo__metodo_private())
# print(f.public)
# print(f.metodo_publico())
