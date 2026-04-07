import sys


def welcome_message() -> None:
    print('Welcome to Groceries!')
    print('Enter:')
    print('----------------------')
    print('1 - To add an item')
    print('2 - To remove an item')
    print('3 - To list all items')
    print('0 - To exit the program')
    print('-----------------------')


def add_item(item: str, groceries: list[str]) -> None:
    groceries.append(item)
    print(f'"{item}" has been added!')

def remove_item(item: str, groceries: list[str]) -> None:
    try:
        groceries.remove(item)
        print(f'"{item}" has been removed!')
    except ValueError:
        print(f'NO "{item}" found in: {groceries}')

def display(groceries: list[str]) -> None:
        print('___List___')
        for i, item in enumerate(groceries):
            print(f'{i}. {item.capitalize()}')

            print('_' * 10)

def is_an_option(text) -> bool:
    return text in ['1', '2', '3', '0']

def main() -> None:
    groceries: list[str] = []

    welcome_message()
    while True:
        user_input: str = input('Choose: ').lower()

        if not is_an_option(user_input):
            print('Please pick a valid option...')
            continue

        if user_input == '1':
            new_items: str = input('What item would you like to add? >> ').lower()
            add_item(new_items, groceries)
        elif user_input == '2':
            item_to_remove: str = input('What item would you like to remove? >> ').lower()
            remove_item(item_to_remove, groceries)
        elif user_input == '3':
            display(groceries)
        elif user_input == '0':
            print('Exiting program...')
            sys.exit()

if __name__ == '__main__':
    main()


















