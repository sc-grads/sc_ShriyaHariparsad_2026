user_input: str = '10'

try:
    result: float = 1 / float(user_input)
    print(f'1 / {user_input} = {result}')
except ValueError:
    print(f'You cannot use: "{user_input}" as a value. ')
except ZeroDivisionError:
    print('Don\'t be silly, you cannot divide by 0. ')
else:
    print('Success! There were no exceptions encountered! ')
finally:
    print('FINALLY: I am always executed!')