import sqlite3
from pathlib import Path

# Configurando o carminho do arquivo
ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD - Create Read    Update Delete
# SQL -  INSERT SELECT  UPDATE DELETE

# CUIDADO: fazendo delete sem where
cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# DELETE mais cuidadoso
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
    f'INSERT INTO {TABLE_NAME} '
    '(name, weight) VALUES'
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

if __name__ == '__main__':
    print(sql)

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "3"'
    )
    connection.commit()

    cursor.execute(
        f'DELETE FROM {TABLE_NAME} '
        'WHERE id = "4"'
    )
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')

    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
