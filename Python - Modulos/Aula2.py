"""
    Criando datas com módulo datetime
    datetime(ano, mês, dia)
    datetime(ano, mês, dia, horas, minutos, segundos)
    datetime.strptime('DATA', 'FORMATO')
    datetime.now()
    https://pt.wikipedia.org/wiki/Era_Unix
    datetime.fromtimestamp(Unix Timestamp)
    https://docs.python.org/3/library/datetime.html
    Para timezones
    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    Instalando o pytz
    pip install pytz types-pytz
"""
from datetime import datetime

data_str_data = '2022/02/13 07:48:56'
data_str_data = '20/04/2023 07:48:56'
data_str_fmt = '%d/%m/%Y %H:%M:%S'

# data = datetime(2022, 4, 20, 21, 45, 13)
data = datetime.strptime(data_str_data, data_str_fmt)
print(data)
