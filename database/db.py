import sqlite3

connection = sqlite3.connect("database/documents.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    pages INTEGER,
    words INTEGER,
    summary TEXT
)
""")

connection.commit()
connection.close()