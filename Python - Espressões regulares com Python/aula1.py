"""
links:
"""
import re

# findall | search | sub
# compile

string = 'Este é um teste de expressões teste regulares.'

print(
    "\tre.search(r'...', variable)",
    re.search(r'teste', string),
    re.search(r'teste2', string),
    sep='\n'
)

print()

print(
    "\tre.findall(r'teste', string)",
    re.findall(r'teste', string),
    re.findall(r'teste2', string),
    sep='\n'
)

print()

print(
    "\tre.sub(r'teste', string)",
    re.sub(r'teste', 'ABCD', string),  # count=1
    re.sub(r'teste2', 'ABCD', string),
    sep='\n'
)

print()

regexp = re.compile(r'teste')

regexp.search(string)
regexp.findall(string)
regexp.sub("ASDASD", string)
