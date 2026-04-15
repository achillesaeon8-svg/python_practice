# Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.

base_number = int(input('Enter a number: '))
exponent_number = int(input('Enter desired exponent: '))

powered_number = base_number ** exponent_number

print(f'The number {base_number} raised to the {exponent_number} results to {powered_number}.')