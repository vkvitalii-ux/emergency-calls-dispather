import sqlite3

def init_db():
    """Создаёт базу данных и таблицу для истории вызовов скорой помощи."""
    conn = sqlite3.connect("медицинские вызовы.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS вызовы (
            номер INTEGER PRIMARY KEY AUTOINCREMENT,
            симптомы TEXT NOT NULL,
            приоритет TEXT NOT NULL,
            бригада TEXT NOT NULL,
            время_создания DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """
    )
    conn.commit()
    conn.close()

def add_call(symptoms: str, priority: str, team_type: str):
    """Добавляет запись о новом вызове в базу данных."""
    conn = sqlite3.connect("медицинские вызовы.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO вызовы (симптомы, приоритет, бригада) VALUES (?, ?, ?)",
            (symptoms, priority, team_type))
    conn.commit()
    conn.close()

