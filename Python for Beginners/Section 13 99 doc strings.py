class User:
    """"
    Base class for creating users.
    """
    def __init__(self, user_id: int) -> None:
        self.user_id = user_id

    def show_id(self) -> None:
        """Prints the user_id"""

        print(self.user_id)

def user_exists(user: User, database: set[User]) -> bool:
    """
    Checks if a user is inside a database.


    :param user: The user to check for
    :param database: the database to check inside
    :return: bool
    """

    return user in database

def main() -> None:
    bob: User = User(0)
    anna: User = User(1)

    database: set[User] = {bob, anna}
    if user_exists(bob, database):
        print('User exists in database!')
    else:
        print('No user found...')

    print(User.__doc__)
    print(user_exists.__doc__)

if __name__ == '__main__':
    main()


