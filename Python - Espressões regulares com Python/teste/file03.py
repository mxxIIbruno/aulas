import re

text = """
Lute com determinação, abrace a vida com paixão, perca com classe e vença com
ousadia, porque o mundo pertence a quem se atreve e a vida é muito para ser
insignificante.

Autor: Augusto Branco
"""

text_compile = re.compile(r'(?:\w+)')
solution = text_compile.findall(text)

print(solution)
