# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

stored_numbers = []

while True:
    inputted_characters = input('Enter a number: ')

    try:
        inputted_numbers = int(inputted_characters)
        stored_numbers.append(inputted_numbers)

        if stored_numbers:
            lowest_number = min(stored_numbers)
            print(f'{lowest_number} is the lowest number.')
    except ValueError:
        print('You had not input a number.')  
        break