# Prog02: Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

stored_numbers = []
duplicated_numbers = []

print('Enter 10 numbers: ')

for numerical_range in range(10): 

    inputted_numbers = int(input(f'Number {numerical_range+1}: '))

    if inputted_numbers in stored_numbers and inputted_numbers not in duplicated_numbers:
        duplicated_numbers.append(inputted_numbers)

    stored_numbers.append(inputted_numbers)

duplicated_range = len(duplicated_numbers)
list.sort(duplicated_numbers)
duplicated_strings = ', '.join(map(str, duplicated_numbers))

if duplicated_range == 1:
    print(f'The duplicated numbers is {duplicated_strings}.')
elif duplicated_range >= 2:
    print(f'The duplicated numbers are {duplicated_strings}.')
else:
    print(f'There are no duplicated.')