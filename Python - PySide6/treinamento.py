from datetime import datetime
from dateutil.relativedelta import relativedelta
import requests


class MyClass:
    def __init__(self, name, surname) -> None:
        self.name = self.set_name(name)
        self.surname = self.set_surname(surname)
        self.age = None

    def set_name(self, name: str):
        return name.strip().title()

    def set_surname(self, surname: str):
        return surname.strip().title()

    def set_age(self, day, month, year):
        date = datetime.now()
        birth = datetime(year, month, day)
        self.age = relativedelta(date, birth).years

    def check_zip_code(self, cep):
        url = f'https://viacep.com.br/ws/{cep}/json'

        try:
            response = requests.get(url)
            response.raise_for_status()

            data_cep = response.json()
            return data_cep
        except requests.exceptions.HTTPError as erro_http:
            print(f'Erro na requisição HTTP: {erro_http}')
        except requests.exceptions.RequestException as erro_req:
            print(f'Erro na requisição: {erro_req}')

    def info(self, value):
        data_cep = self.check_zip_code(value)

        if data_cep:
            print(f'Informações do CEP {value}:\n{data_cep}')
        else:
            print(f'Não foi possível obter informações para o CEP {value}')


if __name__ == '__main__':
    CEP = "01310-100"  # "00000-000"
    my_object = MyClass(
        "name", "surname"
    )
    my_object.set_age(  # Date of Birth
        1,  # Day
        1,  # Month
        9999  # Year
    )
    my_object.check_zip_code(CEP)
    my_object.info(CEP)
