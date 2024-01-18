# Classes decoradoras (Decorator class)

# class Multiplicar:
#     def __init__(self, func) -> None:
#         self.func = func
#         self._multiplicador = 10

#     def __call__(self, *args, **kwds):
#         resultado = self.func(*args, **kwds)
#         return resultado * self._multiplicador


# @Multiplicar
# def soma(x, y):
#     return x * y


class Multiplicar:
    def __init__(self, multiplicador) -> None:
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwds):
            resultado = self.func(*args, **kwds)
            return resultado * self._multiplicador
        return interna



@Multiplicar(2)
def soma(x, y):
    return x * y


dois_mais_quatro = soma(2, 4)
print(dois_mais_quatro)
