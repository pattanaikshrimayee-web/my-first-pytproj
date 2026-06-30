from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    books = cursor.fetchall()

    conn.close()

    html = "<h1>Book List</h1><table border='1'>"
    html += "<tr><th>ID</th><th>Title</th><th>Price</th></tr>"

    for book in books:
        html += f"<tr><td>{book[0]}</td><td>{book[1]}</td><td>{book[2]}</td></tr>"

    html += "</table>"

    return html

if __name__ == "__main__":
    app.run(debug=True)