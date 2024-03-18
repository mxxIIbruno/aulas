"""
    PyMySQL - um cliente MySQL feito em Python Puro
    Doc: https://pymysql.readthedocs.io/en/latest/
    Pypy: https://pypi.org/project/pymysql/
    GitHub: https://github.com/PyMySQL/PyMySQL
"""
import os

import pymysql  # type: ignore
import dotenv

TABLE_NAME = "customers"

dotenv.load_dotenv()

connection = pymysql.connect(
    host=os.environ["MYSQL_HOST"],
    user=os.environ["MYSQL_USER"],
    passwd=os.environ["MYSQL_PASSWORD"],
    database=os.environ["MYSQL_DATABASE"],
    # charset='utf8mb4' # se quiser aplicar o charset aqui também!
)

with connection:
    with connection.cursor() as cursor:
        cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {TABLE_NAME} ("
            "id INT NOT NULL AUTO_INCREMENT, "
            "nome VARCHAR(50) NOT NULL, "
            "idade INT NOT NULL, "
            "PRIMARY KEY (id)"
            ")"
        )
        # CUIDADO: ISSO LIMPA A TABELA
        cursor.execute(f"TRUNCATE TABLE {TABLE_NAME}")
    connection.commit()

    # Começo a manipular dados a partir daqui

    # Inserindo um valor usando placeholders e um iterável
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) VALUES (%s, %s)'
        )
        data = ('Bruno', 45)
        result = cursor.execute(sql, data)
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo um valor usando placeholder e um dicionário
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%(name)s, %(age)s)'
        )
        data2 = {'name': 'Sara', 'age': 23}
        result = cursor.execute(sql, data2)
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo um valor usando placeholder e uma tupla de dicionários
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%(name)s, %(age)s)'
        )
        data2 = ({'name': 'Matheus', 'age': 33},
                 {'name': 'Julia', 'age': 56},
                 {'name': 'Samira', 'age': 24},
                 {'name': 'Ageu', 'age': 74})
        result = cursor.executemany(sql, data2)
        # print(sql, data)
        # print(result)
    connection.commit()

    # Inserindo vários valores usando placeholder e uma tupla de tuplas
    with connection.cursor() as cursor:
        sql = (
            f'INSERT INTO {TABLE_NAME} (nome, idade) '
            'VALUES (%s, %s)'
        )
        data3 = (
            ('Siri', 23),
            ('Cortana', 15),
            ('Samuel', 51)
        )
        result = cursor.executemany(sql, data3)
        # print(sql, data)
        # print(result)
    connection.commit()

    # Lendo os valores com SELECT
    with connection.cursor() as cursor:
        # menor_id = int(input('Digite o menor id:'))
        # maior_id = int(input('Digite o maior id:'))

        menor_id = 2  # int(input('Digite o menor id:'))
        maior_id = 4  # int(input('Digite o maior id:'))

        sql = (
            f'SELECT * FROM {TABLE_NAME} '
            'WHERE id BETWEEN %s AND %s'
        )
        cursor.execute(sql, (menor_id, maior_id))
        # print(cursor.mogrify(sql, (menor_id, maior_id)))
        data5 = cursor.fetchall()

        # for row in data5:
        #     print(row)

    # Apagando com DELETE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'DELETE FROM {TABLE_NAME} '
            'WHERE id = %s'
        )
        cursor.execute(sql, (1, ))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        # for row in cursor.fetchall():
        #     print(row)

    # Editando com UPDATE, WHERE e placeholders no PyMySQL
    with connection.cursor() as cursor:
        sql = (
            f'UPDATE {TABLE_NAME} '
            'SET nome=%s, idade=%s '
            'WHERE id=%s'
        )
        cursor.execute(sql, ('Brasil', 78, 4))
        connection.commit()

        cursor.execute(f'SELECT * FROM {TABLE_NAME} ')

        for row in cursor.fetchall():
            print(row)
