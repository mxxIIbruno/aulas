"""
    Lista de tarefas

    Minha lista vai ter os comandos:
    adicionar, listar, apagar, sair, marcar, limpar
"""
import json
import os


class MyTask:
    """
        Minhas Tarefas

        Ela vai ser em POO (Programação Orientada a Objeto)
    """
    TITLE, STATUS, DESCRITION = 'titulo', 'status', 'descrition'
    with open('preset.json', 'r', encoding='UTF-8') as file:
        COMANDOS = json.load(file)

    def __init__(self) -> None:
        self.data = list()
        self.condition = True
        self.loop()

    def loop(self):
        """
            Função loop

            vai daixar o programa rodando até
            quando o cliente quiser sair do programa
        """
        while self.condition:
            self.show_commands()
            command = input('\nDigite o comando desejado: ').strip()
            self.select_command(command)

    def exit_command(self):
        self.condition = False

    def add_command(self):
        title = input('\nDigite o título da tarefa: ').strip()
        descrition = input('Digite a descrição do mesmo: ').strip()

        self.data.append(
            {title: {
                self.STATUS: False,
                self.DESCRITION: descrition
            }}
        )

        print('\nTarefa adcionada com sucesso!')

    def list_command(self):
        os.system('cls')
        print(
            '########################################################\n' +
            '                        TAREFAS\n'
        )

        if not self.data:
            print(
                '                   Lista está vazia!'
            )
            return

        for item in self.data:
            for task_title, task_datas in item.items():
                status = 'X' if task_datas[self.STATUS] else ' '
                print(
                    f'[{status}] | Titulo: {task_title}'
                    f'\n\tDescrição: {task_datas[self.DESCRITION]}'
                )

    def remove_command(self):
        self.list_command()
        select_task = input('\nDigite o nome da tarefa: ').strip()

        for item in self.data:
            if select_task in item:
                self.data.remove(item)
                print('Tarefa removido com sucesso!')
                return

        print(f'Ops! Não achamos a taréfa "{select_task}"!')

    def mark_command(self):
        self.list_command()
        check_off = input('Digite a taréfa que deseja marcar: ').strip()

        for item in self.data:
            if check_off in item:
                self.mark(item, check_off)
                print('Ação realizada com sucesso!')
                return

        print('Ops! Titulo não encontrado!')

    def mark(self, item, check_off):
        status_atual = self.data[self.data.index(
            item)][check_off][self.STATUS]
        self.data[self.data.index(
            item)][check_off][self.STATUS] = not status_atual

    def select_command(self, value_command: str):
        """
            Assim que o cliente selecionar o comando
            o comando selecionado vai passar pela estrutura condicional
        """
        if value_command in self.COMANDOS:
            print(
                f'\nExecutando: {self.COMANDOS[value_command]}'
            )
            getattr(self, f'{value_command}_command')()
        else:
            print(
                f'\nErro: comando "{value_command}" não existe!'
            )

    def clear_command(self):
        os.system('cls')

    def show_commands(self):
        print(
            '\n########################################################\n' +
            'Comando:', ', '.join(self.COMANDOS)
        )


if __name__ == '__main__':
    my_object = MyTask()
