"""
    Criar uma tela de login
    regitrar usuários nos arquivos e Logar
    
"""
import json
import os


class MyAplication:
    """
        Erro
    """
    __FILE = 'dados.json'

    def __init__(self) -> None:
        self.__date = self.__check_file(self.__FILE)
        self.__loop()

    def __ui_interface(self):
        """
            Apresentar tela Login
        """
        os.system('cls')
        print('\n' + '#' * 60)
        print('\n\t\t\tTela Login')
        print('\n' + '\t\t' + '[1] Login\t[2] Cadastro')
        return input('\n\tDigite o comando: ').strip()

    def __loop(self):
        """
            Enquanto for verdadeiro
        """
        codition_operational = True
        while codition_operational:
            command = self.__ui_interface()
            if command == '1':
                self.__login_user()
            elif command == '2':
                self.__register_user()
            else:
                print(f'Erro: comando desconhecido -> "{command}"!')

    def __check_file(self, file):
        """
            Verificar se o arquivo existe
        """
        if os.path.exists(self.__FILE):
            date = json.load(file)
        else:
            date = dict()
        return date

    def __register_user(self):
        """
            Registra usuario
        """
        with open(self.__FILE, 'w', encoding='UTF-8') as file:
            ...

    def __login_user(self):
        """
            Logar usario existente
        """
        with open(self.__FILE, 'r', encoding='UTF-8') as file:
            date = json.load(file)



if __name__ == '__main__':
    my_object = MyAplication()
