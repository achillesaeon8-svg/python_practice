users_decision = input('Do you want to generate odd numbers only from 0 to 100? Yes or No: ')

if users_decision.lower() == 'yes':
        print('These are all the odd numbers only from 0 to 100:', end=' ')

        number_sequence = 0

        while number_sequence <=99:
            number_sequence += 1
            if number_sequence % 2 != 1:
                continue

            if number_sequence == 99:
                print(number_sequence, end='.')
            else:
                print(number_sequence, end=', ')
elif users_decision.lower() == 'no':
    print('Thank you for considering our generator.')

else:
    print('Invalid input. Please try again.')
