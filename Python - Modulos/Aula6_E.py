"""
    Maria pegou um empréstimo de 1.000.000
    para realizar o pagamento em 5 anos.
    A data em que ela pegou o empréstimo foi
    20/12/2020 e o vencimento de cada parcela
    é no dia 20 de cada mês.
    - Crie a data do empréstimo
    - Crie a data do final do empréstimo
    - Mostre todas as datas de vencimento e o valor de cada parcela
"""
from datetime import datetime

from dateutil.relativedelta import relativedelta


def formatar_data_brasileiro(value):
    fmt = '%d/%m/%Y'
    delta = datetime.strftime(value, fmt)
    return delta


emprestimo_parcelado = 1_000_000 / 60

fmt = '%Y-%m-%d'
data_inicial = datetime.strptime('2020-12-20', fmt)
data_final = datetime.strptime('2025-12-20', fmt)

total_pago = 0
while data_inicial < data_final:
    data_inicial = data_inicial + relativedelta(months=1)
    total_pago += emprestimo_parcelado
    
    print(
        formatar_data_brasileiro(data_inicial) + \
        f' | Pago -> R${emprestimo_parcelado:,.2f}' \
        f' | Total -> R${total_pago:,.2f}'
    )
