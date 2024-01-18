"""
    try, except, else e finally
"""
try:
    print("Abrir Arquivo")
    8/0
except ZeroDivisionError as error:
    print(
        '\nError',
        f'Nome: {error.__class__.__name__}',
        f'Mensagem: {error}\n',
        sep='\n'
    )
finally:
    print("Fechar Arquivo")
    