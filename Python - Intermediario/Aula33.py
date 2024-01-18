"""
    raise - lançando exeções (erros)
"""
def erro_divide_por_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentando dividir por zero!')
    return True


def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado.'
        )
    return True


def divide(n, d):
    erro_divide_por_zero(d)
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    return n / d


print(divide(0, '0'))
