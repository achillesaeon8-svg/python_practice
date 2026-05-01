# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

stored_numbers = []

while True:
    inputted_characters = input('Enter a number: ')

    try:
        inputted_numbers = int(inputted_characters)

    except ValueError:
        print('You had not input a number.')
        break   