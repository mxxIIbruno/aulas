from os import system

system('cls')

perguntas = [
    {
        'pergunta': 'Quanto é 2+2?',
        'opções': ['1', '2', '3', '4'],
        'resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5*5?',
        'opções': ['25', '55', '10', '51'],
        'resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10/2?',
        'opções': ['4', '5', '2', '1'],
        'resposta': '5'
    }
]

for indice, pergunta in enumerate(perguntas, 1):
    questao = pergunta['pergunta']
    option = pergunta['opções']
    resposta = pergunta['resposta']
    print(f'Pergunta - {indice}: {questao}')
    for alt_ind, alternativa in enumerate(option, 1):
        print(f'{alt_ind}) {alternativa}')
    user_input = input('>> ')
    if user_input == resposta:
        print(f'Parabens! A resposta é {resposta}!')
    else:
        print(f'Você errou a resposta é: {resposta}!')
    print()
