from itertools import groupby

NOME, NOTA = 'nome', 'nota'


def ordena(aluno):
    return aluno[NOTA]


alunos = [
    {NOME: 'Luiz', NOTA: 'A'},
    {NOME: 'Letícia', NOTA: 'B'},
    {NOME: 'Fabrício', NOTA: 'A'},
    {NOME: 'Rosemary', NOTA: 'C'},
    {NOME: 'Joana', NOTA: 'D'},
    {NOME: 'João', NOTA: 'A'},
    {NOME: 'Eduardo', NOTA: 'B'},
    {NOME: 'André', NOTA: 'A'},
    {NOME: 'Anderson', NOTA: 'C'},
]

alunos_agrupados = sorted(alunos, key=ordena)
grupos = groupby(alunos_agrupados, key=ordena)

for chave, grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)
