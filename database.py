import sqlite3

DB_PATH = 'passwords.db'

def init_db() -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            password TEXT,
            notes TEXT
        )
    """)
    con.commit()
    con.close()