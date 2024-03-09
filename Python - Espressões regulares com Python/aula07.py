"""
    \w -> [a-zA-Z0-9À-ü_]
    \w -> [a-zA-Z0-9] -> re.A / re.ASCII
    \W -> [^a-zA-Z0-9À-ü_]
    \W -> [a-zA-Z0-9_] -> re.A / re.ASCII
    \d -> [0-9]
    \D -> [^0-9]
    \s -> [ \r\n\f\n\t]
    \b -> borda
    \B -> não borda

    re.A -> ASCII
    re.I -> IGNORECASE
    re.M -> Multiline
    re.S -> Dotall
"""
import re

texto_cpf = '''
131.768.460-53 ASD
055.123.060-50 DEQ
955.123.060-90
'''

texto = '''
João trouxe    flores para sua amada namorada em 10 de janeiro de 1970,
Maria era o nome dela.


Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
maria, hoje sua esposa, ainda faz aquele café com pão de queijo nas tardes de
domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
pão de queijo.
Não canso de ouvir a Maria:
"Joooooooooãooooooo, o café tá prontinho aqui. Veeemm"!
'''

texto_02 = '''
O João gosta de folia
E adora ser amado
'''

# print(re.findall(r'[a-z]+', texto, flags=re.I))
# print(re.findall(r'[a-zA-Z0-9]+', texto))
# print(re.findall(r'[a-zA-Z0-9À-ü]+', texto))
# print(re.findall(r'\w+', texto, flags=re.I))
# print(re.findall(r'\W+', texto, flags=re.I))
# print(re.findall(r'\d+', texto, flags=re.I))
# print(re.findall(r'\D+', texto, flags=re.I))
# print(re.findall(r'\s+', texto, flags=re.I))
# print(re.findall(r'\S+', texto, flags=re.I))
# print(re.findall(r'\be\w+', texto, flags=re.I))
# print(re.findall(r'\w+e\b', texto, flags=re.I))
# print(re.findall(r'\b\w{4}\b', texto, flags=re.I))
# print(re.findall(r'\w{4}', texto, flags=re.I))
# print(re.findall(r'flo\B', texto, flags=re.I))

# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', texto_cpf, flags=re.M))
print(re.findall(r'^o.*o$', texto_02, flags=re.I | re.S))
