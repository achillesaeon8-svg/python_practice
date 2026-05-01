# Prog05: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from lowest to highest. Clue: sort() function.

stored_numbers = []

while True:
    inputted_characters = input('Enter a number: ')

    try:
        inputted_numbers = int(inputted_characters)
        stored_numbers.append(inputted_numbers)

        print(sorted(f'{stored_numbers} these are the numbers that are organized from lowest to highest.'))

    except:
        print('You have not input a number.')
        break