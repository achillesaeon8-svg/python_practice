# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point.

first_number = int(input('Enter your first number: '))
second_number = int(input('Enter a second number: '))

quotient = first_number // second_number

print(f'{quotient} is the quotient of the two numbers.')