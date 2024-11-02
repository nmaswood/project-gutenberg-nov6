import sqlite3


def create_table_if_not_exists():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            book_id INTEGER PRIMARY KEY,
            text TEXT,
            author TEXT,
            title TEXT,
            language TEXT,
            date_published TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recent_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INTEGER
        )
    ''')
    conn.commit()
    conn.close()
