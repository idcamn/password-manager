def print_entries(entries: list[tuple]) -> None:
    """Print entries as a formatted table"""
    if entries:
        header = (
            f"{'[id]':4}"
            f"{'[service]':>12}\t"
            f"{'[login]':>12}\t"
            f"{'[password]':>16}\t"
            f"{'[notes]':>14}"
        )
        print(header)

        for entry_id, service, login, password, notes in entries:
            print(
                f"{entry_id:4}"
                f"{service:>12}\t"
                f"{login:>12}\t"
                f"{password:>16}\t"
                f"{notes:>14}"
            )
    else:
        print('No entries found')