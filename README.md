# Password Manager

Terminal-based password manager written in Python. Stores your credentials locally in SQLite database with no external dependencies.


## Features

- **Add entries** — save a service name, login, password, and optional notes
- **List entries** — view all stored credentials in a table-style list
- **Update entries** — edit any field of an existing entry (or delete that entry)
- **Password generator** — generate cryptographically secure passwords using Python's `secrets` module
  - Guarantees at least one uppercase, lowercase, digit, and symbol
  - Excludes visually ambiguous characters (`O`, `0`, `I`, `l`, `1`) to prevent transcription errors


## Project Structure

```
password-manager/
├── main.py           # entry point
├── core/
│   ├── constants.py  # used constants
│   └── generator.py  # secure password generator
├── db/
│   └── repository.py # database layer (init, CRUD)
└── ui/
    ├── menu.py       # CLI menu I/O
    └── display.py    # formatted table output
```


## Requirements

- Python 3.10+
- No third-party packages — uses only the standard library (`sqlite3`, `secrets`, `string`)


## Getting Started

**1. Clone the repository**

```bash
git clone https://github.com/idcamn/password-manager.git
cd password-manager
```

**2. Run the app**

```bash
python main.py
```

A `passwords.db` database file will be created automatically in the project root on first launch.


## Security Note

> **Currently, this tool stores passwords in plaintext.** It is intended only for learning purposes and local usage.
