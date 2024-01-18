"""
    Módulos padrão do Python (import, from, as e *)
    link: 
(1) inteiro - import nome_modulo
    Vantagens: você tem o namespace do módulo
    Desvantagens: nomes grandes

(2) partes - from nome_modulo import objeto1, objeto2
    Vantagens: nomes pequenos
    Desvantagens: Sem o namespace do módulo

(3) alias 1 - import nome_modulo as apelido
    alias 2 - from nome_modulo import objeto as apelido
    Vantagens: você pode reservar nomes para seu código
    Desvantagens: pode ficar fora do padrão da liguagem

(4) má prática - from nome_modulo import *
    Vantagens: importa tudo de um módulo]
    Desvantafgens: importa tudo de um módulo
"""

# (1)
# import sys

# platform = 'A Minha'
# print(sys.platform)
# print(platform)

# (2)
# from sys import exit, platform

# print(platform)
# exit()

# (3)
# import sys as s

# print(s.platform)
# sys = 'Algo'
# print(sys)
# s.exit()

# (4)
# from sys import *
