# Prog03: Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

while True:
    try:
        inputted_numbers = int(input('Enter a number: '))
        stored_numbers = []
        stored_numbers = inputted_numbers
        
        if inputted_numbers != stored_numbers:
            print('Unique')
        else:
            print('Duplicate')
    except:
        print('You had not input a number.')
        break
