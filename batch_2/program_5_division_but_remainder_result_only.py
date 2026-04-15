# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.

first_number = int(input('Enter your first number: '))
second_number = int(input('Enter a second number: '))

remainder = second_number % first_number

print(f'{remainder} is the remainder of two numbers by dividing the first number to the second number.')