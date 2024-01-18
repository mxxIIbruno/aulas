nome = input('Digite seu nome: ')

tamanho = len(nome)
string_recebe = ''
contador = 0

while contador < tamanho:
    caracter = '*'
    string_recebe += caracter + nome[contador]
    contador += 1
 
print(f'Final: << {string_recebe} >>')
