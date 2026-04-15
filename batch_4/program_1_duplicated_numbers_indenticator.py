# Prog01: Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.

stored_numbers = []
no_duplicated_numbers = []

print('Enter 10 numbers: ')

for numerical_range in range(10): 

    inputted_numbers = int(input(f'Number {numerical_range+1}: '))

    if inputted_numbers in stored_numbers and inputted_numbers not in no_duplicated_numbers:
        no_duplicated_numbers.append(inputted_numbers)

    stored_numbers.append(inputted_numbers)

all_numbers_range = len(no_duplicated_numbers)
list.sort(no_duplicated_numbers)
all_numbers_strings = ', '.join(map(str, no_duplicated_numbers))

if all_numbers_range == 1:
    print(f'The duplicated numbers is {all_numbers_strings}.')
elif all_numbers_range >= 2:
    print(f'The duplicated numbers are {all_numbers_strings}.')
else:
    print(f'There are no duplicated.')