from flask import Flask, render_template, request, redirect
import sqlite3
import tello
from utils import gen_key


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create')
def create_plan():
    return render_template('plan.html')


@app.route('/create', methods=["POST"])
def create_plan_post():
    plan_key = str(gen_key(16))

    connection = sqlite3.connect('plans.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Plans VALUES (?, ?, ?)', (plan_key, "hardcoded desc", "hard coded name"))  # Default flight plan (lift and go)
    cursor.execute('CREATE TABLE IF NOT EXISTS ' + plan_key + ' (FuncCall TEXT, Params INT)')
    for x in request.form.getlist('item'):
        for y in request.form.getlist('select'):
            cursor.execute('INSERT INTO ' + plan_key + ' VALUES (?, ?)', (y, x))
            print(cursor.lastrowid)

    return render_template('plan.html'), connection.commit(), connection.close()


@app.route('/fly')
def fly():
    connection = sqlite3.connect('plans.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM Plans')
    rows = cursor.fetchall()

    return render_template('fly.html', rows=rows)


@app.route('/fly/<name>')
def fly_queries():
    return render_template('fly.html')


if __name__ == '__main__':
    app.run(debug=True)
