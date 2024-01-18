"""
    Faça um programa que peça ao usuário para digitar um número inteiro,
    informe se este número é par ou ímpar. Caso o usuário não digite um número
    inteiro informe que não é um número inteiro
"""
numero_str = input('Digite um número inteiro: ')

try:
    numero_int = int(numero_str)
    if numero_int % 2:
        print(f"O número {numero_int} é ímpar!")
    else:
        print(f'O número {numero_int} é par!')
except:
    print(f"O valor '{numero_str}' não é um número inteiro!")

"""
    Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
    descrito, exiba a saudação apropriada. Ex.
    Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora_str = input("Informe a Hora agora: ")

try:
    hora_int = int(hora_str)
    if 1 <= hora_int <= 11:
        print(f"{hora_int} horas, Bom dia!")
    elif 12 <= hora_int <= 17:
        print(f"{hora_int} horas, Boa tarde!")
    elif 0 <= hora_int <= 23:
        print(f"{hora_int} horas, Boa noite!")
    else:
        print(f"O valor não codis com as horas correspondentes -> {hora_int}")
except:
    print("Precissamos de um número que condis com as horas entre 0 - 23!")

"""
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
    menso escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
    "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""
nome_str = input('Digite seu primeiro nome: ')
tamanho = len(nome_str)

if tamanho < 4:
    print('Seu nome é curto!')
elif 5 <= tamanho <= 6:
    print('Seu nome é normal!')
elif tamanho > 6:
    print('Seu nome é muito grande!')
