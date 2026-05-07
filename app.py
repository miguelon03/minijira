from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    user = {"name": "Juan"}
    return render_template("index.html", usuario=user)

@app.route("/users")
def users():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test_db"
    )
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE active = " + True)
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    app.run(debug=True)