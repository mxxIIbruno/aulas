import os
"""
    Criando arquivo com Python
    Usamos a função open para abrir
    um arquivo em Python (ele pode ou não existir)
    Modos:
    r (leitura), w (escrita), x (para criação)
    a (escreve ao final), b (binário)
    t (modo texto), + (leitura e escrita)
    Context manager - with (abre e fecha)
    Métodos úteis
    write, read (escrever e ler)
    writelines (escrever várias linhas)
    seek (move o cursor)
    readline (ler linha)
    readlines (ler linhas)
    Vamos falar mais sobre o módulo os, mas:
    os.remove ou unlink - apaga o arquivo
    os.rename - troca o nome ou move o arquivo
    Vamos falar mais sobre o módulo json, mas:
    json.dump = Gera um arquivo json
    json.load
"""
caminho_arquivo = 'Aula57.txt'

# arquivo = open(caminho_arquivo, 'w')

# arquivo.close()
# with open(caminho_arquivo, 'w+') as arquivo:
#     print(type(arquivo))
#     for i in range(10):
#         arquivo.write(f'Linha {i}\n')
#     # arquivo.seek(0.0)
#     arquivo.writelines(
#         ('Linha 10\n', 'Linha 11\n')
#     )
#     print(arquivo.read())
#     print('Lendo')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 40)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

# with open(caminho_arquivo, 'a+') as arquivo:
#     print(type(arquivo))
#     for i in range(10):
#         arquivo.write(f'Linha {i}\n')
#     # arquivo.seek(0.0)
#     arquivo.writelines(
#         ('Linha 10\n', 'Linha 11\n')
#     )

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    # print(type(arquivo))
    arquivo.write('Atenção\n')
    for i in range(10):
        arquivo.write(f'Linha {i}\n')
    # arquivo.seek(0.0)
    arquivo.writelines(
        ('Linha 10\n', 'Linha 11\n')
    )

# os.remove(caminho_arquivo)  # os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo, 'aula116.txt')
