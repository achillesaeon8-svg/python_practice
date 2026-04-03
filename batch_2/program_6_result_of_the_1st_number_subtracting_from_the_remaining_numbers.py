selected_numbers = 0

print('Enter 10 numbers: ')

for numerical_range in range(1, 11):
    while True:
        try:
                
            inputted_numbers = int(input(f'Enter number {numerical_range}: '))
            if numerical_range == 1:
                selected_numbers = inputted_numbers
            else:
                selected_numbers -= inputted_numbers

            break
            
        except ValueError:
            print('Invalid Input. Please try again.')            

print(f'{selected_numbers} is the result of subtracting the first number you had inputted to the remaining numbers.')