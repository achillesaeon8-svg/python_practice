# Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop).

users_decision = input('Do you want to generate even numbers only from 0 to 100? Yes or No: ')

if users_decision.lower() == 'yes':
        print('These are all the even numbers only from 0 to 100:', end=' ')

        for number_sequence in range(2, 101, 2):

            if number_sequence == 100:
                print(number_sequence, end='.')
            else:
                print(number_sequence, end=', ')

elif users_decision.lower() == 'no':
    print('Thank you for considering our generator.')

else:
    print('Invalid input. Please try again.')
