from abstract_for_age import ABCForAge
from variables import Variables


class Age(ABCForAge, Variables):
    def __init__(self):
        self.message()
        super().__init__()
        self.display_solution()

        print(
            '------------------------FIM------------------------'
        )

    def message(self):
        welcome_message = self.date.strftime(
            '\t\tHoje é dia %d de %B de %Y!'
        )
        print(
            welcome_message,
            '---------------------------------------------------',
            sep='\n'
        )

    def set_year(self) -> int:
        while self.birth_year is None:
            insert = input('Ano de nascimento: ')
            self.birth_year = insert
            if self.birth_year is not None:
                return self.birth_year
            print(
                f'\tAno invalido: digite um ano entre [1500 - {self.date.year}]!\n'
            )

    def set_month(self) -> int:
        while self.birth_month is None:
            insert = input('Mês de nascimento: ').strip()
            self.birth_month = insert
            if self.birth_month is not None:
                return self.birth_month
            print(
                '\tMês invalido: digite um mês entre [1 - 12]\n'
            )

    def set_day(self) -> int:
        while self.birth_day is None:
            insert = input('Dia de nascimento: ').strip()
            self.birth_day = insert
            if self.birth_day is not None:
                return self.birth_day
            print(
                '\tDia invalido: digite o dia correspondente ao mês!',
                f'\tEscolha o dia entre [1 - {self.month_day}]!', sep='\n'
            )

    def display_solution(self):
        print(
            '---------------------------------------------------',
        )
        init_message = self.birth_date.strftime('Você nasceu no dia %d de %B de %Y')
        print(
            init_message,
            f'Idade: {self.age.years} anos',
            f'Mês(es): {self.age.months} mês(es) ao total!',
            f'Dia(s): {self.age.days} dia(s).', sep='\n'
        )
