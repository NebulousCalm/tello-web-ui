import random
import string
import sqlite3


def gen_key(val):
    return ''.join(random.choice(string.ascii_letters) for character in range(val))


def run_plan(table_name):
    file = open('DONTOUCH.py', 'w')
    file.write('from tello import *')
    file.write('start()')
    connection = sqlite3.connect('plans.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM ' + table_name)
    rows = cursor.fetchall()
    for row in rows:
        file.write('')
    return print(rows), connection.commit(), connection.close()
