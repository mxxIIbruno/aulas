import re


def format_cpf(cpf):
    # Remover qualquer caractere não numérico do CPF
    cpf_numerico = re.sub(r'\D', '', cpf)

    # Aplicar a expressão regular para formatar o CPF
    cpf_formatado = re.sub(
        r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf_numerico
    )

    return cpf_formatado


# Exemplo de uso
CPF = "00000000000"
cpf_formatado = format_cpf(CPF)
print(cpf_formatado)
