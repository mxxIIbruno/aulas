import re


def get_number(value=''):
    regexp = re.compile(r'\d+')

    return ''.join(regexp.findall(value))


def fmt_cpf(value: str):
    # Refatorar linha de código | ERRO
    fmt = re.findall(
        r'\d{3}\.\d{3}\.\d{3}-\d{2}',
        value
    )

    return fmt


text = """
Número: 12345678912
Nome: Bruno
"""

number = get_number(text)
cpf = fmt_cpf(number)

print(cpf)
