"""
    Meta caracteres: ^ $ ( )
    [@#a-zA-Z0-9]+
    (abc|def)
"""
import re
from pprint import pprint

texto = '''
<p>Frase 1 </p> <p>Frase 2 </p> <p>Frase 3 </p> <div>Frase 4 </div>
'''

# cpf = '123.456.789-01'
# pprint(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<([pdiv]{1,3})>(?:.*?)<\/\1>', texto)
# tags = re.findall(r'<(?P<tag>[pdiv]{1,3})>(?:.*?)<\/(?P=tag)>', texto)
# pprint(tags)

pprint(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1"\3"\4', texto))

# # for tag in tags:
# #     um, dois = tag
# #     print(um, dois)
