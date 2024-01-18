from os import system


class GameHangman:
    __gameOver = True

    def __init__(self):
        self.game_options()

    @staticmethod
    def clear():
        system('cls')

    @staticmethod
    def title():
        message = 'Palavra Secreta'
        print(f'\n{message:^85}\n')

    def game_options(self):
        condition = True
        while condition:
            self.clear()
            self.title()
            print('Opções: [1]Sair [2]Jogar')
            user_input = input('>> ')
            if user_input.isdigit():
                if user_input == '1':
                    self.__gameOver = False
                    condition = not condition
                    continue
                elif user_input == '2':
                    self.__gameOver = True
                    condition = not condition
                    continue
                print('Segue as opções indicadas!')
            else:
                print('Segue as opções indicadas!')


game = GameHangman()
