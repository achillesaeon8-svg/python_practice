stored_numbers = []
distinct_numbers = []

print('Enter 10 numbers: ')

for numerical_range in range(10): 
    while True:
        try:

            inputted_numbers = int(input(f'Number {numerical_range+1}: '))
            stored_numbers.append(inputted_numbers)

            break

        except ValueError:
            print('Invalid input. Please try again.')

for inputted_numbers in stored_numbers:
    if stored_numbers.count(inputted_numbers) == 1:
        distinct_numbers.append(inputted_numbers)

distinct_range = len(distinct_numbers)
list.sort(distinct_numbers)
distinct_strings = ', '.join(map(str, distinct_numbers))

if distinct_range == 1:
    print(f'The distinct numbers is {distinct_strings}.')
elif distinct_range >= 2:
    print(f'The distinct numbers are {distinct_strings}.')
else:
    print(f'There are no distinct.')    