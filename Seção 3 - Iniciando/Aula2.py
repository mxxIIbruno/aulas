"""
    parametro sep -> separador 
    CRLF - > 'Carriage Return Line Feed' isso é uma quebra de linha especifica do Windows
    \r\n - > \r=return, \n=line feed
    \n -> LF 'Existe no MAC'
"""

print(12, 34, sep="-", end="\r\n")
print(56, 78, sep='-', end='\n')
print(9, 10, sep="-", end='\n')
