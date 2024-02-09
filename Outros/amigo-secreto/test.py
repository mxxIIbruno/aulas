"""
    Code:
"""
from random import randint

messagen = []
for i in range(5):
    num = randint(0, 80)
    if str(num) in messagen:
        num
    messagen.append(str(num))

print(
    "\nNúmeros aleatorios: ", end=''
)
print(' - '.join(sorted(messagen)) + '\n')
