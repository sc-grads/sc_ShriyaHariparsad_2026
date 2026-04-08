def start_program(db: dict[int, str]) -> None:
    assert db, 'Database is empty'

    print('Loaded:', db)
    print('Program started successfully!')

def main() -> None:
    db1: dict[int, str] = {0: 'a', 1: 'b'}
    start_program(db=db1)

if __name__ == '__main__':
    main()


