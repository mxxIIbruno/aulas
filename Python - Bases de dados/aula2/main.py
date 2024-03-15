"""
    PyMySQL - um cliente MySQL feito em Python Puro
    Doc: https://pymysql.readthedocs.io/en/latest/
    Pypy: https://pypi.org/project/pymysql/
    GitHub: https://github.com/PyMySQL/PyMySQL
"""
import os

import pymysql
import dotenv

dotenv.load_dotenv()

connection = pymysql.connect(host=os.environ['MYSQL_HOST'],
                             user=os.environ['MYSQL_USER'],
                             passwd=os.environ['MYSQL_PASSWORD'],
                             database=os.environ['MYSQL_DATABASE'])
with connection:
    cursor = connection.cursor()

    # SQL
    print(cursor)
    ...
