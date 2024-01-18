"""
    Usando calendar para calendários e datas
    https://docs.python.org/3/library/calendar.html
    calendar é usado para coisas genéricas de calendários e datas.
    Com calendar, você pode saber coisas como:
    - Qual o último dia do mês (ex.: monthrange)
    - Qual o nome e número do dia de determinada data (ex.: weekday)
    - Criar um calendário em si (ex.: monthcalendar)
    - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
    Por padrão dia da semana começa em 0 até 6
    0 = segunda-feira | 6 = domingo
"""
import calendar

# print(calendar.calendar(2024))
# print(calendar.month(2022, 12))
# print(calendar.monthrange(2024, 1))
# print(list(calendar.day_name))

# indice, dia = calendar.monthrange(2024, 1)
# print(
#     f'Vai ser no numa {list(calendar.day_name)[indice]} ' +\
#         f'e ele tem ao todo {calendar.weekday(2024, 1, dia)} dias.'
# )
# print(calendar.monthcalendar(2024, 1))
# for semanas in calendar.monthcalendar(2024, 1):
#     for dia in semanas:
#         print(
#             f'{dia:>2}', end='|'
#         )
#     print()
