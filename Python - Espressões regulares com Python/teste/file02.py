import re
from pprint import pprint

input_a = 'a0y1y2eby3sd4rt5fe67i8wgsa9l0'
get_number = re.sub(r"\D", r"", input_a)

format_cpf = re.sub(
    r'([0-9]{3})([0-9]{3})([0-9]{3})([0-9]{2})',
    r'\1.\2.\3-\4', get_number
)

pprint(format_cpf)
