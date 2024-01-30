from datetime import datetime

from dateutil.relativedelta import relativedelta

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('02/10/1996 12:13:45', fmt)
data_final = datetime.strptime('13/01/2024 18:10:45', fmt)
delta = relativedelta(data_final, data_inicio)
print(
    delta.years, delta.months, delta.days,
    delta.hours, delta.minutes, delta.seconds
)
# delta = timedelta(days=10, hours=2)
# print(data_final + delta)
print(data_final)
print(data_final + relativedelta(seconds=59, minutes=10))

# delta = data_final - data_inicio
# print(
#     f'Dias: {delta.days}\n' \
#     f'Segundos: {delta.seconds}\n' \
#     f'Micorsegundos: {delta.microseconds}\n'
# )
# print(delta.total_seconds())

# print(data_final > data_inicio)
# print(data_final < data_inicio)
# print(data_final == data_inicio)
