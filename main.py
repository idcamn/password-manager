import sqlite3
import secrets
import string

def generate_password(length: int = 12) -> str:
    if not isinstance(length, int):
        raise TypeError("Password length must be an integer")
    if length < 4:
        raise ValueError("Password length must be >= 4")

    symbols = '()[]!@#$^&_?+-*/={}:;'

    # Guarantee every symbol at least once
    guaranteed = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.digits),
        secrets.choice(symbols)
    ]

    pool = string.ascii_letters + string.digits + symbols
    res = [secrets.choice(pool) for _ in range(length - 4)] + guaranteed
    secrets.SystemRandom().shuffle(res)
    return ''.join(res)


def show_menu():
    print("\tLocal Password Manager")
    print("\thelp - get available cmds")
    input("> ")


def show_help():
    print("help - show help")
    print("list - view all passwords")
    print("add - add new password")
    print("update - update password")
    print("quit - quit")
    print("")


def main():
    # add auth
    show_menu()


if __name__ == '__main__':
    main()