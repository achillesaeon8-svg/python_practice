# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function.

stored_numbers = []

while True:
    inputted_characters = input('Enter a number: ')

    try:
        inputted_numbers = int(inputted_characters)
        stored_numbers.append(inputted_numbers)

    except:
        print('You have not input a number.')

        if stored_numbers:
            stored_numbers.sort()
            if len(stored_numbers) == 1:
                ascending_order_numbers = str(stored_numbers[0])
                print(f'{ascending_order_numbers} this is the number that is input which is organized from lowest to highest.')

            else:
                ascending_order_numbers = ', '.join(map(str, stored_numbers[:-1]))
                last_number = stored_numbers[-1]
                multiple_inputted_numbers = f'{ascending_order_numbers}, and {last_number}'
                print(f'{multiple_inputted_numbers} these are the numbers that are input which are organized from lowest to highest.')

        break