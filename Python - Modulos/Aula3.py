"""
    datetime.timedelta e dateutil.relativetimedelta (calculando datas)
    Docs:
    https://dateutil.readthedocs.io/en/stable/relativedelta.html
    https://docs.python.org/3/library/datetime.html#timedelta-objects
"""
from datetime import datetime

# from pytz import timezone

data = datetime.now()
print(data.timestamp()) # Isso está n base de dados
print(datetime.fromtimestamp(1705160065.754809))

# ['America/Sao_Paulo', 'Asia/Tokyo']
# data = datetime.now(timezone('Asia/Tokyo'))

# data = datetime(2022, 4, 20, 21, 45, 13, tzinfo=timezone('Asia/Tokyo'))
# data = datetime.strptime(data_str_data, data_str_fmt)
