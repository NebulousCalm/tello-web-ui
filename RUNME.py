import sqlite3
from utils import gen_key

connection = sqlite3.connect('plans.db')
cursor = connection.cursor()

default_plan = str(gen_key(16))

cursor.execute("CREATE TABLE IF NOT EXISTS Plans (UniqueKey NOT NULL PRIMARY KEY,  Description TEXT, PlanName TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS " + default_plan + " (FuncCall TEXT, Params INT)")
cursor.execute('INSERT INTO Plans VALUES (?, ?, ?)', (default_plan, "Example flight plan for your first", "First Flight"))  # Default flight plan (lift and go)
cursor.execute('INSERT INTO ' + default_plan + ' VALUES (?, ?)', ('takeoff', 0))

connection.commit()
connection.close()
