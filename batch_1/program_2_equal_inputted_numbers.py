# Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.

first_number = float(input('Enter your first number: '))
second_number = float(input('Enter a second number: '))

if first_number == second_number:
    print('Both numbers are equal.')
elif first_number != second_number:
    print('Both numbers are not equal.')
else:
    print('Incorrect input.')