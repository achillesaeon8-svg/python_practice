# Prog02: Create a program that ask user to input 2 numbers. Print "Not Equal" when the numbers are not the same.

first_number = int(input('Enter your first number: '))
second_number = int(input('Enter a second number: '))

if first_number == second_number:
    print('Both numbers are equal.')
elif first_number != second_number:
    print('Both numbers are not equal.')
else:
    print('incorrect input.')