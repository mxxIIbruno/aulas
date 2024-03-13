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
    f'INSERT INTO {TABLE_NAME} (id, name, weight) VALUES'
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
# cursor.execute(sql, {'nome': 'Joana', 'peso': 4})
cursor.executemany(
    sql,
    (
        {'nome': 'Joana', 'peso': 4},
        {'nome': 'Bruno', 'peso': 5},
    )
)


connection.commit()
print(sql)

cursor.close()
connection.close()
