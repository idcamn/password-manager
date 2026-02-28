import sqlite3

DB_PATH = 'passwords.db'

def init_db() -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute("""
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT,
            login TEXT,
            password TEXT,
            notes TEXT
        )
    """)
    con.commit()
    con.close()


def add_password(service: str, login: str, password: str, notes: str = '') -> None:
    con = sqlite3.connect(DB_PATH)
    con.execute(
        """
        INSERT INTO passwords (service, login, password, notes)
        VALUES (?, ?, ?, ?)
        """, 
        (service, login, password, notes),
    )
    con.commit()
    con.close()