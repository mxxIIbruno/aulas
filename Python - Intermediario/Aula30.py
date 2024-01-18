# Try, except, else e finally
try:
    a = 18
    b = 0
    print('Linha 1')
    
    c = a / b
    print('Linha 2')
except NameError as error:
    print(error)
except ZeroDivisionError as error:
    print(error)
except TypeError as error:
    print(error)
except Exception as error:
    print(error)

print('CONTINUAR')
