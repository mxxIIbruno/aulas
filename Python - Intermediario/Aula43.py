"""
    Funções decoradoras e decoradores
    Decorar = Adicionar / Remover / Restringir / Alterar
    Funções decoradoras são funções que decoram outras funções
    Decoradores são usados para fazer o Python 
    usar as funções decoradoras em outras funções.
    Decoradores são "Syntax Sugar" (Açúcar sintático)
"""
def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        resultado += 'QUALQUER'
        print(f'O seu resultado foi {resultado}')
        print('OK, agora você foi decorada')
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(paramentro):
    if not isinstance(paramentro, str):
        raise TypeError('parametro deve ser uma string')


# inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string('Bruno')
print(invertida)
