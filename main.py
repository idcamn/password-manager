import sqlite3
import secrets
import string

def generate_password(length: int = 12) -> str:
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
    print("Type 'help' to get available cmds")


def show_help():
    print("list - view all passwords")
    print("add - add new password")
    print("update - update password")
    print("quit - quit")


def show_list():
    print("not implemented yet")


def show_add():
    print("not implemented yet")


def show_update():
    print("not implemented yet")


def main():
    # add auth
    show_menu()
    while True:
        cmd = input('> ').lower()
        if not cmd:
            continue
        if cmd == 'quit':
            break
        elif cmd == 'help':
            show_help()
        elif cmd == 'list':
            show_list()
        elif cmd == 'add':
            show_add()
        elif cmd == 'update':
            show_update()
        else:
            print("Unknown command. Type 'help' to get available commands")

if __name__ == '__main__':
    main()