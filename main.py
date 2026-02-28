import sqlite3
import secrets

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