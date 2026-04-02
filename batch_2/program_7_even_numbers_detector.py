numbers = 0

print('Enter 10 integer numbers: ')

for i in range(1, 11): 
    while True:
        try:

            inputted_numbers = int(input(f'Number {i}: '))

            if inputted_numbers % 2 == 0:
                numbers += 1
                
            break

        except ValueError:
            print('Invalid input. Please try again.')
    
print(f'There are {numbers} total even numbers detected')