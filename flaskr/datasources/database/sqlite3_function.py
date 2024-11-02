import sqlite3


def entry_book(book_id, text, author, title, language, date_published):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO books (book_id, text, author, title, language, date_published) VALUES (?, ?, ?, ?, ?, ?)
''', (book_id, text, author, title, language, date_published))
    conn.commit()
    conn.close()


def get_book(book_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE book_id = ?
    ''', (book_id,))
    data = cursor.fetchone()
    conn.close()
    if not data:
        return None
    return {'text': data[1], 'metadata': {'author': data[2], 'title': data[3], 'language': data[4], 'date_published': data[5]}}


def get_book_metadata(book_ids):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM books WHERE book_id IN ({})
    '''.format(','.join('?' for _ in book_ids)), book_ids)
    data = cursor.fetchall()
    conn.close()
    return [{'book_id': row[0], 'author': row[2], 'title': row[3], 'language': row[4], 'date_published': row[5]} for row in data]


def entry_activity(book_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT OR IGNORE INTO recent_activity (book_id) VALUES (?)
    ''', (book_id,))
    conn.commit()
    conn.close()


def get_recent_activity():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM recent_activity
    ''')
    data = cursor.fetchall()
    conn.close()
    book_ids = [row[1] for row in data]
    return get_book_metadata(book_ids)