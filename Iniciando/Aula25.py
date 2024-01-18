"""
    CONSTANTE = "Variáveis que não vão mudar
    Muitas condições no mesmo if (ruim)
        <- Contagem de complexidade (ruim)
"""
from random import randint
from time import sleep

RADAR_1 = 60        # velocidade máxima do radar 1
LOCAL_1 = 100       # local onde o radar 1 está
RADAR_RANGE = 1     # A distância onde o radar pega

local_carro = 0
quantidade = 0

while True:
    velocidade = randint(1, 120)     # velocidade atual do carro
    
    local_carro += velocidade / 2    # local em que o carro está na estrada
    quantidade += 1
    if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
        local_carro <= (LOCAL_1 + RADAR_RANGE and \
                    velocidade > RADAR_1):
        print('\nPassou da velocidade permitida!')
        
        print(f'Velocidade do carro: {velocidade}')
        print(f'Local do carro: {local_carro}\n')
        print(quantidade)
        break

    if local_carro > RADAR_RANGE + LOCAL_1:
        local_carro = 0
        quantidade = 0
