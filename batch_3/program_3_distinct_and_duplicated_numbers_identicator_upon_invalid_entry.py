# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.
stored_numbers = []

while True:
    inputted_characters = input('Enter a number: ')

    try:

        inputted_numnbers = int(inputted_characters)
        
        if inputted_characters in stored_numbers:
            print('Duplicate')
        else:
            print('Unique')
    except ValueError:
        print('You had not input a number.')
        break   