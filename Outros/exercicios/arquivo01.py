"""
    Problema:
        Escreva um programa em Python que solicite ao usuário que insira uma
        lista de números separados por vírgula e, em seguida, calcule e exiba a
        média desses números.
"""
import re
from pprint import pprint

message_1 = "Insera uma lista de números separados por vírgula "
message_2 = "EX: 10,20,30,40,50: "
message = message_1 + message_2

input_user = input(message)
input_user = re.findall(r'\d+(?:\.?\d+)', input_user)

input_user = [float(x) for x in input_user]

pprint(
    'A média dos números inseridos é: '
    f'{sum(input_user) / len(input_user):,.2f}'
)
