def executa(funcao, *args):
    return funcao(*args)


def soma(x, y):
    return x + y


def cria_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


if __name__ == '__main__':
    duplica = cria_multiplicador(2)
    duplica = executa(
        lambda m: lambda n: n * m,
        2
    )

    print(
        executa(
            lambda x, y: x *y,
            2, 3
        )
    )


