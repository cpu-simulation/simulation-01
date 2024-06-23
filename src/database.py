import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS memory (
        address TEXT PRIMARY KEY,
        value TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS registers (
        name TEXT PRIMARY KEY,
        value TEXT
    )
    ''')

    conn.commit()
    conn.close()
