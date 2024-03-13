import sqlite3
from pathlib import Path

# Configurando o carminho do arquivo
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

# Configurando nome da tabela
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)
cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)
connection.commit()

# Criando a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
# CUIDADO: sql injection
sql = (
    f'INSERT INTO {TABLE_NAME} (name, weight) VALUES'
    # '(NULL, ?, ?)'
    '(:name, :peso)'
)
# cursor.execute(sql, ['Joana', 8.6])
# cursor.executemany(
#     sql,
#     [
#         ['Joana', 8.6],
#         ['Bruno', 5.6]
#     ]
# )
cursor.execute(sql, {'name': 'Marcos', 'peso': 10})
cursor.executemany(
    sql,
    (
        {'name': 'Joana', 'peso': 4},
        {'name': 'Bruno', 'peso': 5},
        {'name': 'Sem nome', 'peso': 3},
        {'name': 'Maria', 'peso': 8},
        {'name': 'Helena', 'peso': 9},
    )
)
connection.commit()

cursor.close()
connection.close()

if __name__ == '__main__':
    print(sql)
