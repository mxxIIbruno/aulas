# Try, except, else e finally
try:
    a = 18
    b = 0
    # print(b[0])
    # print('Linha 1'[1000])
    
    c = a / b
    print('Linha 2')
except NameError as error:
    print('Nome:', error.__class__.__name__)
    print('MSG:', error)
except ZeroDivisionError as error:
    print('Nome:', error.__class__.__name__)
    print('MSG:', error)
except (TypeError, IndexError) as error:
    print('Nome:', error.__class__.__name__)
    print('MSG:', error)
except Exception as error:
    print('Nome:', error.__class__.__name__)
    print('MSG:', error)

print('CONTINUAR')
