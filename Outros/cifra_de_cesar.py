"""
    Code: Cifra de Cesar
"""
import string

# variaveis iniciais
ALPHA = string.ascii_letters + \
    string.digits + ' ' + string.punctuation
KEY = 3
MESSAGE_SIZE = len(ALPHA)

# menssagem do usuario
message = input('\nDigite sua mensagem: ').strip()

# nova mensagem cifrada
new_message = ''

# operação para nova mensagem
for letter in message:
    get_index = ALPHA.index(letter)
    cesar_encryption = ALPHA[(get_index + KEY) % MESSAGE_SIZE]
    new_message += cesar_encryption

print(f'Mensagem Criptografada: {new_message}\n')
