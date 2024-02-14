"""
    10          * 9 = 90
    90          * 8 = 750
    750         * 7 = 5.040
    5.040       * 6 = 30.240
    30.240      * 5 = 151.200
    151.200     * 4 = 604.800
    604.800     * 3 = 1.814.400
    1.814.400   * 2 = 3.628.800
    3.628.800   * 1 = 3.628.800
"""

from os import system

system('cls')


def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)


numero = 10
reusltado = fatorial(numero)
print(f'O fatorial de {numero} é {reusltado}!')

# num_a = 10
# num_b = num_a

# while num_a > 1:
#     num_a -= 1
#     num_b *= num_a

# print(num_b)
