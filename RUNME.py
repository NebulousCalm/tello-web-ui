import sqlite3

connection = sqlite3.connect('plans.db')
cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Plans (UniqueKey NOT NULL PRIMARY KEY, PlanName TEXT, Description TEXT, Plan TEXT)")
# cursor.execute("INSERT INTO Plans VALUES ()") Default flight plan (lift and go)
