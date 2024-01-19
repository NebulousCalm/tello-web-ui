from flask import Flask, render_template, request, redirect
import sqlite3
import tello


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/create')
def create_plan():
    return render_template('plan.html')


@app.route('/create', methods=["POST"])
def create_plan_post():
    connection = sqlite3.connect('plans.db')
    cursor = connection.cursor()
    for x in request.form.getlist('item'):
        for y in request.form.getlist('select'):
            print(y, x)

    return render_template('plan.html'), connection.commit(), connection.close()


if __name__ == '__main__':
    app.run(debug=True)
