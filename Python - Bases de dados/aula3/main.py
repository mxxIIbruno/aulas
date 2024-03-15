"""
    PyMySQL - um cliente MySQL feito em Python Puro
    Doc: https://pymysql.readthedocs.io/en/latest/
    Pypy: https://pypi.org/project/pymysql/
    GitHub: https://github.com/PyMySQL/PyMySQL
"""
import pymysql

connection = pymysql.connect(host='localhost',
                             user='usuario',
                             passwd='senha',
                             database='base_de_dados')
with connection:
    cursor = connection.cursor()

    # SQL
    print(cursor)
    ...
