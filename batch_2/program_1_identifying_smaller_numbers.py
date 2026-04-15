# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

first_number = float(input('Enter your first number: '))
second_number = float(input('Enter a second number: '))

if first_number > second_number:
    print(first_number, 'is the smaller number.')
else:
    print(second_number, 'is the smaller number.')