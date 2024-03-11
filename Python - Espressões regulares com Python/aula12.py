"""
    https://regex101.com/r/HTKy5p/1
"""
import re

senha_forte_regexp = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@[-`{-~]).{12,}$",
    flags=re.M
)

string = """
VÁLIDAS
uUw^PJ`@32g0
Sl|RS.zm107{
Jg6eH~g3=7K}
2q{2k3j.Z{QO
;g6Rc6{Gw;T1

SEM MINÚSCULAS
K3354N}V+*}P
ZW4L:$<$82N1
0]T6IR'~0]N4
)'S91{G01A?H
;K<6U~4^9ON3

SEM MINÚSCULAS E NÚMEROS
PE'~ROG<.L\<
\K_IQ]JFE)|;
<QRO](&}AN?T
}B<VSRI[={F]
AA;R|}C*>Y?A

SEM MINÚSCULAS, CARACTERES E NÚMEROS
MKQZVCEXVYXF
BMKYMYBIHXPQ
EJBEHVLKXQMA
LPLPCFWTZQKD
JOYSPVXDUZOD

QUANTIDADE INVÁLIDA (6)
?D5ni6
4hq0Z:
4Wb{j6
?3g0mB
G6r0e`
"""

print(senha_forte_regexp.findall(string))
