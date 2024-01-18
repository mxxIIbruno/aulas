"""
    Intrudução ao try/except
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar
"""
str_numero_entrada = input('Vou dobraro número que você digitar: ')

try:
    numero = float(str_numero_entrada)
except ValueError:
    print('Isso não é um número!')

if numero is not None:
    numero *= numero
    print(f'O dobro de {str_numero_entrada} é {numero:,.2f}')
