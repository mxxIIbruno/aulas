from os import system


def listar(tarefa):
    print()
    if not tarefa:
        print('Não ha uma tarefa para listar!')
        return
    
    print('TAREFAS:')
    for t in tarefa:
        print(t)


def desfazer(tarefa, desfazer_tarefas):
    print()
    if not tarefa:
        print('Não ha uma tarefa para desfazer!')
        return
    
    desfazer_tarefas.append(tarefa.pop())


def refazer(tarefa, refazer_tarefa):
    if not refazer_tarefa:
        print('Não tem nehuma tarefa para refazer!')
        return
        
    tarefa.append(refazer_tarefa.pop())


tarefas =[]
tarefas_desfeitas =[]
comandos_feitos = []

operacional = True
while operacional:
    print('\nComando: listar, limpar, desfazer e refazer.')
    tarefa_escolhida = input('Digite uma tarefa ou comando: ')

    if not tarefa_escolhida:
        operacional = not operacional
        continue
    elif tarefa_escolhida == 'limpar':
        system('cls')
    elif tarefa_escolhida == 'listar':
        listar(tarefas)
    elif tarefa_escolhida == 'desfazer':
        desfazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
        comandos_feitos.append(tarefa_escolhida)
    elif tarefa_escolhida == 'refazer':
        refazer(tarefas, tarefas_desfeitas)
        listar(tarefas)
        comandos_feitos.append(tarefa_escolhida)
    else:
        tarefas.append(tarefa_escolhida)
        listar(tarefas)

"""
Tarefa para criar um arquivo Json fazer o aplicativo ler e salvar as informações
"""
