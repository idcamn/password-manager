import sqlite3


DB_PATH = 'passwords.db'


def init_db() -> None:
    """Create the passwords table if it does not exist"""
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


def create_entry(service: str, login: str, password: str, notes: str = '') -> None:
    """Insert a new entry into the database"""
    with sqlite3.connect(DB_PATH) as con:
        con.execute("""
            INSERT INTO passwords (service, login, password, notes)
            VALUES (?, ?, ?, ?)
        """, (service, login, password, notes))


def list_entries() -> list[tuple]:
    """Load all entries ordered by id"""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("""
            SELECT id, service, login, password, notes
            FROM passwords
            ORDER BY id
        """)
        return cur.fetchall()
    

def get_entry(entry_id: int) -> tuple | None:
    """Load a single entry by its id"""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("""
            SELECT id, service, login, password, notes 
            FROM passwords 
            WHERE id = ?
        """, (entry_id,))
        return cur.fetchone()


def delete_entry(entry_id: int) -> bool:
    """Delete an entry by id"""
    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute("""
            DELETE 
            FROM passwords 
            WHERE id = ?
        """, (entry_id,))
        return cur.rowcount > 0
    

def update_entry(entry_id: int, column: str, value: str) -> bool:
    """Update a selected column value by id"""
    allowed_columns = {"service", "login", "password", "notes"}
    if column not in allowed_columns:
        raise ValueError("Invalid column name")

    with sqlite3.connect(DB_PATH) as con:
        cur = con.execute(f"""
            UPDATE passwords 
            SET {column} = ? 
            WHERE id = ?
        """, (value, entry_id))
        return cur.rowcount > 0