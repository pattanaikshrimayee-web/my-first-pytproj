import sqlite3

def save_book(title, price):
    conn = sqlite3.connect("books.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        price TEXT
    )
    """)

    cursor.execute(
        "INSERT INTO products (title, price) VALUES (?, ?)",
        (title, price)
    )

    conn.commit()
    conn.close()