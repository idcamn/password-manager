import sqlite3
import secrets
import string

def generate_password(length: int = 8) -> str:
    pool = string.ascii_letters + string.digits + '()[]!@#$^&_?+-*/={}:;'
    return ''.join(secrets.choice(pool) for _ in range(length))


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