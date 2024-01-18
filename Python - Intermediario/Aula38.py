import importlib

import Aula38_m

print(Aula38_m.variavel)

for i in range(10):
    importlib.reload(Aula38_m)
    print(i)

print('FIM')
