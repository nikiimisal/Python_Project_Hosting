
from flask import Flask, request, render_template
import mysql.connector

app = Flask(__name__)

#  MySQL connection

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="nikhil"
    )
    cursor = db.cursor()

@app.route('/')
def home():
    return render_template('forms.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, email, password))
    db.commit()

    return f"User {name} registered successfully!"

if __name__ == '__main__':
    app.run(debug=True)
