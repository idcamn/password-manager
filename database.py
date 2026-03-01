import sqlite3

DB_PATH = 'passwords.db'

def init_db() -> None:
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            CREATE TABLE IF NOT EXISTS passwords (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                service TEXT,
                login TEXT,
                password TEXT,
                notes TEXT
            )
        """)


def add_password(service: str, login: str, password: str, notes: str = '') -> None:
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            INSERT INTO passwords (service, login, password, notes)
            VALUES (?, ?, ?, ?)
            """, 
            (service, login, password, notes),
        )


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
        return cur.rowcount > 0
    

def edit_by_id(row_id: int, column_name: str, new_value: str) -> bool:
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute(f"UPDATE passwords SET {column_name} = ? WHERE id = ?", (new_value, row_id),)
        return cur.rowcount > 0