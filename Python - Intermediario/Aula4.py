"""
    Escopo de funções em Python 
    Escopo significa o local onde aquele código pode atingir.
    Existe o escopo  global e local.
    O escopo global é o escopo onde todo o código é alcançavel.
    O escopo local é o escopo onde apenas nomes do mesmo local
    podem ser alcaçados.
"""
x = 1

def escopo():
    global x
    x = 10
    y = 2

    def outra():
        x = 10
        global y
        y = 13
        print(x, y)
    outra()
    print(x)
    
print(x)
escopo()
print(x)
print(y)
