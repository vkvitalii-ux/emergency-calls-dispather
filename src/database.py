import sqlite3

def init_db():
    """Создает базу данных и таблицу для истории вызовов скорой помощи."""
    conn = sqlite3.connect("medical_calls.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS calls (
            id INTEGER PRIMARY KEY AUTOINCREMENT ,
            symptoms TEXT NOT NULL,
            priority TEXT NOT NULL,
            brigade TEXT NOT NULL,
            created-at DATETIME DEFAULT CURRENT""")