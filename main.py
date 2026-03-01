import secrets
import string
import database as db
from constants import (SAFE_UPPERCASE, SAFE_LOWERCASE, SAFE_DIGITS, SAFE_SYMBOLS)

def generate_password(length: int = 12) -> str:
    if length < 4:
        raise ValueError("Password length must be >= 4")

    # Guarantee every symbol at least once
    guaranteed = [
        secrets.choice(SAFE_UPPERCASE),
        secrets.choice(SAFE_LOWERCASE),
        secrets.choice(SAFE_DIGITS),
        secrets.choice(SAFE_SYMBOLS)
    ]

    pool = SAFE_UPPERCASE + SAFE_LOWERCASE + SAFE_DIGITS + SAFE_SYMBOLS
    res = [secrets.choice(pool) for _ in range(length - 4)] + guaranteed
    secrets.SystemRandom().shuffle(res)
    return ''.join(res)


def show_menu() -> None:
    print("[Main Menu]")
    print("Type 'cmds' to get available commands")
    while True:
        cmd = input('> ').lower()
        if not cmd:
            continue
        if cmd in ['quit', 'q']:
            quit()
        elif cmd == 'cmds':
            show_cmds()
        elif cmd == 'list':
            show_list()
        elif cmd == 'add':
            show_add()
        elif cmd == 'update':
            show_update()
        else:
            print("Unknown command. Type 'cmds' to get available commands")


def show_cmds() -> None:
    print("[Commands]")
    print("cmds - view available commands")
    print("list - view all passwords")
    print("add - add new password")
    print("update - update password")
    print("quit - exit program")


def show_list() -> None:
    # TODO: change output, make it look nice
    print("[Passwords List]")
    pw_data = db.list_entries()
    print(pw_data)
    # TODO: if asked, copy password by id


def show_add() -> None:
    print("[Add New Password]")
    print("Type 'yes' to continue")
    ans = input("> ").lower()
    if ans in ['yes', 'y']:
        data_service = input('Enter service name: ')
        data_login = input('Enter login: ')
        pw_ans = input('Enter password manually (1) or generate it (2): ')
        if pw_ans == '2':
            data_password = generate_password(12)
            print(f"Generated password: {data_password}")
            # TODO: Copy password to clipboard
        else:
            data_password = input('Password: ')
        data_notes = input('Enter notes (optional): ')
        db.create_entry(data_service, data_login, data_password, data_notes)
        print('Success!')


def show_update() -> None:
    # FIXME: raising valueerror if input != int, add checks for empty/non-digit input
    print("[Update Password]")
    entry_id = int(input('Enter ID (from passwords list): '))
    row = db.get_entry(entry_id)
    while row is None:
        entry_id = int(input('Incorrect ID! Enter correct ID (or 0 to return): '))
        if entry_id == 0:
            return
        row = db.get_entry(entry_id)
    entry_id, service, login, password, notes = row

    # random widths that I liked while testing
    print(f"{'[id]':4}{'[service]':>12}\t{'[login]':>12}\t{'[password]':>16}\t{'[notes]':>14}")
    print(f"{entry_id:4}{service:>12}\t{login:>12}\t{password:>16}\t{notes:>14}")
    
    print("Available actions: u(pdate), d(elete)")
    ans = input('Enter action: ').lower()
    while ans not in ['update', 'u', 'delete', 'd']:
        ans = input('Incorrect action! Enter again (or 0 to return): ').lower()
        if ans == '0':
            return
    if ans in ['update', 'u']:
        column = input('Enter column to edit: ').lower()
        while column not in ['service', 'login', 'password', 'notes']:
            column = input('Incorrect column name! Enter column to edit: ').lower()
        value = input('Enter new value: ')
        res = db.update_entry(entry_id, column, value)
        print('Update success!' if res else 'Something went wrong..')
    elif ans in ['delete', 'd']:
        confirm = input("Are you sure? Type 'yes' to continue: ").lower()
        if confirm in ['yes', 'y']:
            res = db.delete_entry(entry_id)
            print('Deletion success!' if res else 'Something went wrong..')


def main() -> None:
    # add auth
    db.init_db()
    show_menu()


if __name__ == '__main__':
    main()