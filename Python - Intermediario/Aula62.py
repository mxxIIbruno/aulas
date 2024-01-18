"""
    Controlando a quantidade de argumentos posicionais e nomeados em funções
    *args (ilimitado de argumentos posicionais)
    **kwargs (ilimitado de argumentos nomeados)
    (1) Positional only Parameters (/) - Tudo antes da barra deve ! APENAS ! posicional.
    PEP 570 - Python Positional-Only Parameters
    link: ________________________________________________________
    (2) Keyword-Only Arguments (*) - * sozinho ! NÃO SUGA ! valores.
    PEP 3102 - Keyword-Only Arguments
    link:_________________________________________________________
"""
def soma(a, b, *, c):
    print(a + b + c)


# def soma(a, b, /, c):
#     print(a + b + c)


soma(1, 2, c=3)
