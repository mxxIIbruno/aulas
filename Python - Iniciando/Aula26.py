"""
    Flag (Bandeira) - Marcar um local
    None = Não valor
    is e is not = é ou não é (tipo, valor, identidade)
    id = indentidade
"""

# v1 = 'a'
# v2 = 'a'

# print(f"Variavel v1 guarada: {v1}, Espaço da memoria: {id(v1)}")
# print(f"Variavel v2 guarada: {v2}, Espaço da memoria: {id(v2)}")

condition = False
passou_no_if = None

if condition:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não Faça algo')

if passou_no_if is None:
    print('Não passou no if')
else:
    print("Passou no if")
