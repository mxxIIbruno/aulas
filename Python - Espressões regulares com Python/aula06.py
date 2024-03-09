"""
    Meta caracteres: ^ $
    ^ -> começa com
    $ -> termina com
    [^a-z] -> Negação
"""
import re

cpf = 'a 123.456.789-01'
code_01 = re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})$', cpf)
code_02 = re.findall(r'[^0-9a-zA-Z.-]+', cpf)

print(code_01)
print(code_02)
