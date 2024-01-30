"""
    sys.argv - Executando arquivos com argumentos no sistema
    Font = Fire Code

    Informações adicionais:
    Comando:
        -> cls ; venv/bin/python -m pip install "modulo"
        descrição: instala um módulo sem você ativar o ambiente virtual
        -> cls ; venv/bin/python "arquivo.py"
        descrição: abrir o arquivo no ambiente virtuaL
"""
import sys

# print(sys.argv)

argumentos = sys.argv
qtd_argumentos = len(argumentos)

# print(qtd_argumentos)

if qtd_argumentos <= 1:
    print('Você não passou argumentos')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça alguma coisa com {argumentos[2]}')
    except IndexError:
        print('Falta argumentos!')
