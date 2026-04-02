total: int = 0

print('Welcome to Calc+! Add positive numbers, or insert "0" to exit.')
while True:
    user_input: int = int(input('Enter a number: '))

    if user_input < 0:
        print('!!!Please enter positive numbers only!!!')
        continue

        if user_input == 0:
            print(f'Total: {total}')
            break

            total += user_input

