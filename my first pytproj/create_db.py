import sqlite3

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
    ("Python Book", "500")
)

conn.commit()
conn.close()

print("Database and table created successfully!")