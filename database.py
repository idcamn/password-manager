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


def load_passwords() -> list[tuple]:
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("""
            SELECT id, service, login, password, notes
            FROM passwords
            ORDER BY id
        """)
        return cur.fetchall()
    

def load_by_id(row_id: int) -> tuple | None:
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("SELECT id, service, login, password, notes FROM passwords WHERE id = ?", (row_id,),)
        return cur.fetchone()


def delete_by_id(row_id: int) -> bool:
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("DELETE FROM passwords WHERE id = ?", (row_id,),)
        return cur.rowcount > 0 # returns True if row deleted, else False