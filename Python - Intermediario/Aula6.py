from os import system
import sys
from string import ascii_lowercase


class GameHangman:
    __gameOver = True
    __secret_word = None
    __lettles_player = ''

    def __init__(self) -> None:
        self.__game_options()
        self.__init_game()

    @staticmethod
    def __clear():
        system('cls')

    @staticmethod
    def __title():
        message = 'Palavra Secreta'
        print(f'\n{message:^85}\n')

    def __default_settings(self):
        self.__clear()
        self.__title()

    def __game_options(self):
        condition = True
        self.__title()
        while condition:
            message = 'Opções: [1]Jogar [2]Sair'
            print(message)
            user_input = input('>> ')
            
            if user_input == '1':
                self.__gameOver = True
                condition = not condition
                self.__secret_word = input('Digite a paravra secreta: ')
                continue
            if user_input == '2':
                self.__gameOver = False
                condition = not condition
                continue
            else:
                self.__default_settings()
                print('Segue as instruções para continuar!')
    
    def __init_game(self):
        self.__default_settings()

        while self.__gameOver:    
            field_for_secret_word = ''
            error = 0
            for field in self.__secret_word:
                if field.count(' ') or field.count('-'):
                    field_for_secret_word += field
                elif field.lower() in self.__lettles_player:
                    field_for_secret_word += field 
                else:
                    field_for_secret_word += '_'
            
            for letter in self.__lettles_player:
                if letter not in self.__secret_word.lower():
                    error += 1
                
            if field_for_secret_word == self.__secret_word:
                self.__lettles_player = ''
                self.__default_settings()
                print('Parabens você acertou!')
                print(f'A palavra secreta é: {self.__secret_word}')
                print(f'Você errou {error}x!')
                self.__game_options()
                continue

            print(f'Qual é a palavra?\t\t\t-> {field_for_secret_word}')
            
            user_input = input('Digite uma letra: ')
            
            if len(user_input) > 1:
                self.__default_settings()
                print(f'Precisamos de uma letra, você digitou "{user_input}"!')
            elif user_input not in ascii_lowercase + '1234567890ç':
                self.__default_settings()
                print('Precisamos de uma letra ou algo que possa compor a palavra secreta!')
                print(f'Você digitou "{user_input}"!')
            else:
                self.__default_settings()
                self.__lettles_player += user_input

            sys.exit()


var_game = GameHangman()
