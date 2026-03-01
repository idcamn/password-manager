import secrets
import string
import database as db


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


def show_menu() -> None:
    print("\tLocal Password Manager")
    print("Type 'help' to get available cmds")
    while True:
        cmd = input('> ').lower()
        if not cmd:
            continue
        if cmd in ['quit', 'q']:
            quit()
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


def show_help() -> None:
    print("help - view available commands")
    print("list - view all passwords")
    print("add - add new password")
    print("update - update password")
    print("quit - quit")


def show_list() -> None:
    pw_data = db.load_passwords()
    print(pw_data)
    # TODO: if asked, copy password by id


def show_add() -> None:
    print("[add new password]")
    print("type 'yes' to continue")
    ans = input("> ").lower()
    if ans in ['yes', 'y']:
        data_service = input('service: ')
        data_login = input('login: ')
        pw_ans = input('generate password (1) or insert manually (2): ')
        if pw_ans == '1':
            data_password = generate_password(12)
            print(f"generated password: {data_password}")
        else:
            data_password = input('password: ')
        data_notes = input('notes (optional): ')
        db.add_password(data_service, data_login, data_password, data_notes)
        print('success!')


def show_update() -> None:
    row_id = int(input('enter row id: '))
    row = db.load_by_id(row_id)
    while row is None:
        row_id = int(input('incorrect id! enter correct id (or 0 to exit): '))
        if row_id == 0:
            return
        row = db.load_by_id(row_id)
    idx, service, login, password, notes = row
    print(f"{'[id]':4}{'[service]':>12}\t{'[login]':>12}\t{'[password]':>16}\t{'[notes]':>14}")
    print(f"{idx:4}{service:>12}\t{login:>12}\t{password:>16}\t{notes:>14}")
    
    # TODO: edit output, currently its very ugly :\
    print('u - update; d - delete; e - exit')
    ans = input('select action: ').lower()
    while ans not in ['u', 'd', 'e']:
        ans = input('incorrect action! choose again: ').lower()
    
    if ans == 'u':
        column = input('enter column to edit: ').lower()
        while column not in ['service', 'login', 'password', 'notes']:
            column = input('incorrect value! enter column name to edit: ').lower()
        value = input('enter new value: ')
        res = db.edit_by_id(row_id, column, value)
        print('success!' if res else 'something went wrong..')
    elif ans == 'd':
        confirm = input("are you sure? type 'yes' to continue: ").lower()
        if confirm in ['yes', 'y']:
            res = db.delete_by_id(row_id)
            print('row deleted!' if res else 'something went wrong..')


def main() -> None:
    # add auth
    db.init_db()
    show_menu()


if __name__ == '__main__':
    main()