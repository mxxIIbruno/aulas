def multiplicar(resultado):
    num_1 = 0
    num_2 = 0

    dicionario_de_resultados = {}
    while num_2 < 101:
        if num_1 == 11:
            num_1 = 0
            num_2 += 1
            continue
        resultado_da_funcao = num_1 * num_2
        if resultado_da_funcao == resultado:
            dicionario_de_resultados_x = {}
            dicionario_de_resultados_x['a'] = num_1
            dicionario_de_resultados_x['b'] = num_2
            dicionario_de_resultados_x['x'] = resultado_da_funcao
            dicionario_de_resultados.update(dicionario_de_resultados_x.copy())
        num_1 += 1


def subtrair(resultado):
    num_1 = 0
    num_2 = 0

    dicionario_de_resultados = {}
    while num_2 < 101:
        if num_1 == 11:
            num_1 = 0
            num_2 += 1
            continue
        resultado_da_funcao = num_1 - num_2
        if resultado_da_funcao == resultado:
            dicionario_de_resultados_x = {}
            dicionario_de_resultados_x['a'] = num_1
            dicionario_de_resultados_x['b'] = num_2
            dicionario_de_resultados_x['x'] = resultado_da_funcao
            dicionario_de_resultados.update(dicionario_de_resultados_x.copy())
        num_1 += 1


def somar(resultado):
    num_1 = 0
    num_2 = 0

    dicionario_de_resultados = {}
    while num_2 < 101:
        if num_1 == 11:
            num_1 = 0
            num_2 += 1
            continue
        resultado_da_funcao = num_1 + num_2
        if resultado_da_funcao == resultado:
            dicionario_de_resultados_x = {}
            dicionario_de_resultados_x['a'] = num_1
            dicionario_de_resultados_x['b'] = num_2
            dicionario_de_resultados_x['x'] = resultado_da_funcao
            dicionario_de_resultados.update(dicionario_de_resultados_x.copy())
        num_1 += 1


def dividir(resultado):
    num_1 = 0
    num_2 = 0

    dicionario_de_resultados = {}
    while num_2 < 101:
        if num_1 == 11:
            num_1 = 0
            num_2 += 1
            continue
        resultado_da_funcao = num_1 / num_2
        if resultado_da_funcao == resultado:
            dicionario_de_resultados_x = {}
            dicionario_de_resultados_x['a'] = num_1
            dicionario_de_resultados_x['b'] = num_2
            dicionario_de_resultados_x['x'] = resultado_da_funcao
            dicionario_de_resultados.update(dicionario_de_resultados_x.copy())
        num_1 += 1


def caucular(operador, resultado):
    if operador == '-':
        subtrair(resultado)
    if operador == '+':
        somar(resultado)
    if operador == '/':
        dividir(resultado)
    if operador == '*':
        multiplicar(resultado)


operador = None
resultado_final = None

ligado = True
while ligado:
    if operador is None:
        operador = input('Digite o operador: ')
    if operador not in '-/+*':
        print(f'\n{operador} <- Operador não existe!')
        operador = None
        continue
    
    if resultado_final is None:
        resultado_final = input('Digite o resultado final: ')
        try:
            resultado_final = int(resultado_final)
        except:
            print(f'\n{resultado_final} <- Resultado não aceito!')
            resultado_final = None
            continue
        
    ligado = not ligado

caucular(operador, resultado_final)
