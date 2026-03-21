users_decision = input('Do you want generate even numbers only from 0 to 100? Yes or No: ')

if users_decision.lower() == 'yes':
        print('These are all the even numbers only from 0 to 100:', end=' ')

        for i in range(2, 101, 2):
            print(i, end=' ')

elif users_decision.lower() == 'no':
    print('Thank you for considering our generator.')

else:
    print('Invalid input. Please try again.')
