"""
    https://regex101.com/r/NY9nqU/1

    Minha Solução antes da revisão:
    "^(?:[+-]{,1})[0-9]+(?:\.?)(?:[0-9]+)$"

    Solução do professor:
    "^[+-]?\d+(?:\.\d+)?$"
"""
import re

text = """
Válidos
0.0
00.00
000.000
+0.0
-00.00
+000.000
10
50
8.5
-8.5
+10.5005412136
1231345458.54654564
-133215646589.6543215648978977
+1.11123123
-0.154987
1.121654987
10.123
10.1
-1.1

Inválidos
10..2
++1213
--1235050
.124546
-.1231324
10.
.1
.10
10.
+10.
-10.
5a
b5
"""


def is_float(value):
    return bool(re.search(
        r'^(?:[+-]{,1})[0-9]+(?:\.?)(?:[0-9]+)$',
        value
    ))


def is_int(value):
    return bool(re.search(
        r'^(?:[+-]{,1})[0-9]+$',
        value
    ))


while True:
    input_user = input('Digite um número: ')

    if is_int(input_user):
        input_user = int(input_user)
        print(f'O número {input_user} foi convertido para int.')
        continue

    if is_float(input_user):
        input_user = float(input_user)
        print(f'O número {input_user} foi convertido para float.')
