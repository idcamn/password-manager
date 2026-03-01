from db.repository import init_db
from ui.menu import show_menu


def main() -> None:
    # add auth
    init_db()
    show_menu()


if __name__ == '__main__':
    main()