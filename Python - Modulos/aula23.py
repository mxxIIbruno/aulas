# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula21-ex.csv'
lista_clientes = [{
    'Nome': 'Luiz Otávio',
    'Endereco': 'Av 1, 22'
}, {
    'Nome': 'João Silva',
    'Endereço': 'R. 2"1"'
}, {
    'Nome': 'Maria Sol',
    'Endereço': 'Av B, 3A'
}]

# lista_clientes = [['Luiz Otávio', 'Av 1, 22'], ['João Silva', 'R. 2"1"'],
#                   ['Maria Sol', 'Av B, 3A']]
with open(CAMINHO_CSV, 'w', encoding='utf8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    # nome_colunas = ['Nome', 'Endereço']
    escritor = csv.DictWriter(arquivo, fieldnames=nome_colunas)
    escritor.writeheader()

    for cliente in lista_clientes:
        escritor.writerow(cliente)
        # escritor.writerow(cliente.values())
