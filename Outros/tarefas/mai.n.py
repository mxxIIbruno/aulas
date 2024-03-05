from os import system
from pathlib import Path
import os

ROOT_ADDRES = Path(__file__).parent
FILE = ROOT_ADDRES / 'sav.txt'
ENCODING = 'UTF-8'

lista_do_arquivo = []
lista_segundaria = []


def listar():
    with open(FILE, 'r', encoding=ENCODING) as arquivo:
        print('\nTAREFAS:')
        for linha in arquivo.readlines():
            print(linha, end='')


def adicionar(text):
    with open(FILE, 'a+', encoding=ENCODING) as arquivo:
        tarefa = text + '\n'
        lista_do_arquivo.append(tarefa)
        arquivo.write(tarefa)


def desfazer(lista, desfar_tarefa):
    if not lista:
        print('\nTarefa vazia não ah como desfazer!')
        return

    desfar_tarefa.append(lista.pop())
    print('\nTarefa desfeita!')

    with open(FILE, 'w', encoding=ENCODING) as arquivo:
        arquivo.write("")

    with open(FILE, 'a+', encoding=ENCODING) as arquivo:
        for linha in lista:
            arquivo.write(linha)


def refazer(lista, lista_refazer):
    if not lista_refazer:
        print('\nNão é possivel refazer tarefa!')
        return

    tarefa = lista_refazer.pop()
    lista.append(tarefa)

    print('\nAção refeita com sucesso!')
    with open(FILE, 'a+', encoding=ENCODING) as arquivo:
        arquivo.write(tarefa)


def iniciar():
    if not os.path.exists(FILE):
        with open(FILE, 'w', encoding=ENCODING):
            ...

    if not lista_do_arquivo:
        with open(FILE, 'r', encoding=ENCODING) as arquivo:
            items = arquivo.readlines()
            for i in items:
                lista_do_arquivo.append(i)


operational = True
while operational:
    iniciar()
    print(os.name)
    print('\nComando: listar, refazer, desfazer, limpar.')
    instruction = input('Digite uma tarefa ou comando: ')

    if not instruction:
        operational = not operational
        system('clear')
        print('Aplicativo foi fechado!')
    elif instruction == 'limpar':
        if os.name == 'nt':
            system('cls')
        else:
            system('clear')
    elif instruction == 'listar':
        listar()
    elif instruction == 'desfazer':
        desfazer(lista_do_arquivo, lista_segundaria)
    elif instruction == 'refazer':
        refazer(lista_do_arquivo, lista_segundaria)
    else:
        adicionar(instruction)
