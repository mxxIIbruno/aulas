"""
    CPF: 746.824.890-70
    Colete a soma dos 9 primeiros dígitos do CPF
    multiplicando cada um dos vaolres por uma
    contagem regressiva começando de 10

    Ex.: 746.824.890-70 (746824890)
        10  9   8   7   6   5   4   3   2
    *   7   4   6   8   2   4   8   9   0
        70  36  48  56  12  20  32  27  0
    
    Somar todos os resultados:
    70+36+48+56+12+20+32+27+0 = 301
    Multiplicar o resultado anterior por 10
    301 * 10 = 3010
    Obter o resto da divisão da conta anterior por 11
    3010 % 11 = 7
    Se o resultado anterior for maior que 9:
        resultado é 0
    contrário disso:
        resultado é o valor da conta

    O primeiro dígito do CPF é 7

    Faz a mesma Operação com o digito a mais
    em vez de começar do 10 começe do 11 para obter o ultimo digito.
"""
import re
import sys


# sys.exit()

cpf_original = '451.280.108-13'
# var_value = re.sub(r'[^0-9]', '', '451.280.108-13')
# cpf_original = '451.280.108-13'.replace('.', '').replace('-', '')
cpf_confirma = ''

for triagem in cpf_original:
    if triagem.isdigit() and len(cpf_confirma) < 9:
        cpf_confirma += triagem

DEZ = 10

for vezes in range(2):
    num_1 = DEZ + vezes
    count = 0
    
    for indice, valor in enumerate(cpf_confirma):
        mult = num_1 - indice
        count += mult * int(valor)
    
    passo_1 = count * DEZ
    passo_2 = passo_1 % 11

    if passo_2 > 9:
        cpf_confirma += '0'
    else:
        cpf_confirma += str(passo_2)
    
print(cpf_confirma)
