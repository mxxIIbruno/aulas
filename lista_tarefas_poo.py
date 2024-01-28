"""
    Lista de tarefas

    Minha lista vai ter os comandos:
    adicionar, listar, apagar, sair, marcar, limpar
"""
import os


class MyTask:
    """
        Minhas Tarefas

        Ela vai ser em POO (Programação Orientada a Objeto)
    """
    __T, __S, __D = 'titulo', 'status', 'descrition'
    # variaveis da classe
    __data = [
        {__T: {
            __S: False,
            __D: 'texto'
        }}
    ]
    __condition = True

    def __init__(self) -> None:
        self.__loop()

    def __loop(self):
        """
            Função loop

            vai daixar o programa rodando até
            quando o cliente quiser sair do programa
        """
        while self.__condition:
            self.__show_commands()
            command = input('Digite o comando desejado: ')
            self.__select_command(command)

    def __exit_command(self):
        self.__condition = False

    def __add_task(self):
        var_title = input('\nDigite o título da tarefa: ')
        var_descrition = input('Digite a descrição do mesmo: ')

        self.__data.append(
            {var_title: {
                'status': False,
                'descrition': var_descrition
            }}
        )

        print('\nTarefa adcionada com sucesso!')

    def __list_command(self):
        os.system('cls')
        print(
            '########################################################\n' +
            '                        TAREFAS\n'
        )

        if not self.__data:
            print(
                '                   Lista está vazia!'
            )
            return

        for item in self.__data:
            item: dict

            for datas_k, datas_v in item.items():
                var_status = 'X' if datas_v[self.__S] else ' '
                var_descrition = datas_v[self.__D]

                print(
                    f'[{var_status}] | Titulo: {datas_k}'
                    f'\n\tDescrição: {var_descrition}'
                )

    def __remove_command(self):
        self.__list_command()
        select_task = input('\nDigite o nome da tarefa: ').strip()

        for item in self.__data:
            if select_task in item:
                self.__data.remove(item)
                print('Tarefa removido com sucesso!')
                return

        print(f'Ops! Não achamos a taréfa "{select_task}"!')

    def __mark_command(self):
        self.__list_command()
        check_off = input('\nDigite a taréfa que deseja marcar: ').strip()

        for item in self.__data:
            if check_off in item:
                self.__mark(item, check_off)
                print('Ação realizada com sucesso!')
                return

        print('Ops! Titulo não encontrado!')

    def __mark(self, item, check_off):
        status_atual = self.__data[self.__data.index(
            item)][check_off][self.__S]
        self.__data[self.__data.index(
            item)][check_off][self.__S] = not status_atual

    def __select_command(self, value_command: str):
        """
            Assim que o cliente selecionar o comando
            o comando selecionado vai passar pela estrutura condicional
        """
        if value_command == 'sair':
            print('\nAté a proxima!\n')
            self.__exit_command()
        elif value_command == 'limpar':
            os.system('cls')
        elif value_command == 'adicionar':
            self.__add_task()
        elif value_command == 'listar':
            self.__list_command()
        elif value_command == 'apagar':
            self.__remove_command()
        elif value_command == 'marcar':
            self.__mark_command()
        else:
            print(
                f'\nErro: comando "{value_command}" não existe!'
            )

    def __show_commands(self):
        print(
            '\n########################################################\n' +
            'Comando: sair, limpar, adicionar, listar, apagar, marcar\n'
        )


if __name__ == '__main__':
    my_object = MyTask()
