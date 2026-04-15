# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.

chosen_numbers = 0

print('Enter 10 numbers: ')

for numerical_range in range(1, 11):
    while True:
        try:

            inputted_numbers = int(input(f'Enter number {numerical_range}: '))
            chosen_numbers += inputted_numbers

            break

        except ValueError:
            print('Invalid Input. Please try again.')
                
print(f'The sum of all 10 numbers are {chosen_numbers}.')