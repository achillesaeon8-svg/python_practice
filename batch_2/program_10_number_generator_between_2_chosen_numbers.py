print('Enter 2 numbers: ')
first_number = int(input('Enter your first number: '))
second_number = int(input('Enter your second number: '))

minimal_number = min(first_number, second_number)
maximum_number = max(first_number, second_number)

numbers_between = maximum_number - minimal_number

if numbers_between == 2:
    print(f'The number between {first_number} and {second_number} is', end=' ')
elif numbers_between >= 3:
    print(f'The numbers between {first_number} and {second_number} are', end=' ')
else:
    print(f'There are no numbers between {first_number} and {second_number }.')

for numerical_range in range(minimal_number + 1, maximum_number): 
    if numerical_range == maximum_number - 1:
        print(numerical_range, end='.')
    else:
        print(numerical_range, end=', ')