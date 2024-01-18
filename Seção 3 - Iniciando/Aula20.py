"""
                    Operadores lógicos
    and (e) or (ou) not (não)
    and - Todas as condições precisam ser verdadeiras.
    Se qualquer valor for considerado falso,
    a expressão inteira será avaliada naquele valor
    São considerados falsy (que você ja viu) 0, 0.0, '', False
    Também existe o tipo None que é usado para representar um não valor.
"""
entrada = input('[E]ntrar [S]air: ').upper()
senha_digitada = input('Senha: ')

senha_permitida = '12345678'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou')
elif entrada == 'S':
    print('Você saiu')
else:
    print('Você não inseriu nem [E] ou [S] para entrar ou sair!')
