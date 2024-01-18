palavra = '123321'

palindromo = [palavra[x] for x in range(len(palavra) -1, -1, -1)]
palavra = list(palavra)

if palavra == palindromo:
    print('São palindromos')
else:
    print('Não são palindromos!')
