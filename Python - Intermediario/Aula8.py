"""
    Exercícios com funções

    Crie uma função que multiplica todos os arugumentos
    não nomeados recebidos
    Retorne o total para uma variável e mostre o valor
    da variável.

    Crie uma função fala se um número é par ou ímpar.
    Retorne se o número é par ou ímpar
"""

def mult(*args):
    count = 0
    num = args[-1]
    for i in args:
        count += num * i
        num = i
    return count

def par_or_impar(num):
    return 'ímpar' if num % 2 else 'par'

variavel_a = mult(1, 2, 3)
print(variavel_a)
variavel_b = par_or_impar(variavel_a)
print(variavel_b)
