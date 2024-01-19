import random
import string
import sqlite3
import os


def gen_key(val):
    return ''.join(random.choice(string.ascii_letters) for character in range(val))


def filters(func, param):
    param = str(param)
    # shitty logic
    append = open('DONTOUCH.py', 'a+')
    if func == "Takeoff":
        return append.write('takeoff()\n'), append.close()
    elif func == "Forward":
        return append.write('forward(' + param + ')\n'), append.close()
    elif func == "Backward":
        return append.write('backward(' + param + ')\n'), append.close()
    print(func, param)


def run_plan(table_name):
    file = open('DONTOUCH.py', 'w')
    file.write('from tello import *\n')
    file.write('start()\n')
    connection = sqlite3.connect('plans.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM ' + table_name)
    rows = cursor.fetchall()
    file.close()
    for row in rows:
        filters(row[0], row[1])
    fileEnding = open('DONTOUCH.py', 'a+')
    fileEnding.write('land()\n')
    return connection.commit(), connection.close()  # os.system('python3 DONTOUCH.py')  USE THIS TO RUN DRONE UNCOMMENT THIS AFTER DEVELOPMENT
