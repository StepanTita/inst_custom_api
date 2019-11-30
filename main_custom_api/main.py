import os
import click
from api import get_inst_data
from csv_writer import put_user_data


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    again = True

    while again:
        clear_console()
        again = False

        print('Enter username:')
        username = str(input())
        user = get_inst_data(username, False)

        if user is None:
            print("Invalid username!")
            again = True
            continue

        if click.confirm('Is it fake or spammer account?', default=True):
            user.is_fake = True

        put_user_data(user)

        if click.confirm('Check another user?', default=True):
            again = True
