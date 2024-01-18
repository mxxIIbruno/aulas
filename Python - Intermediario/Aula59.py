# Problema dos parâmetros mutáveis em funções Python
def adicina_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 =  adicina_clientes('luis')
adicina_clientes('Bruno', cliente1)
adicina_clientes('Cerezo', cliente1)
cliente1.append('Edu')
print(cliente1)

cliente2 =  adicina_clientes('Tereza')
adicina_clientes('Santos', cliente2)
print(cliente2)
