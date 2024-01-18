texto_1 = 'Calculadora infinito'.title()
print(f'{texto_1:^50}')

condicao = True
contador = 0

while condicao:
    numero = input('Digite um número: ').replace(',', '.')
    try:
        numero = float(numero)
        condicao = not condicao
    except ValueError as error:
        print(error)
        print(f'<< {numero} >> Não é um número!')    

while condicao != 'N':
    mensagem = f'\n{numero} x {contador} = {contador * numero}'
    print(mensagem)
    condicao = input('Sair? [S]im - [N]ão: ').upper()
    contador += 1
