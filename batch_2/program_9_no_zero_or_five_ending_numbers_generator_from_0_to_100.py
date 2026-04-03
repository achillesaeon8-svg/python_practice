users_decision = input('Do you want to distinguish all numbers starting from 0 to 100 except numbers ending 0 or 5? Yes or No: ')

if users_decision.lower() == 'yes':
    for number_sequence in range(101):
        
        if str(number_sequence).endswith('0'):
            continue
        elif str(number_sequence).endswith('5'):
            continue
        if number_sequence == 99:
            print(number_sequence, end='.')
        else:
            print(number_sequence, end=', ')

elif users_decision.lower() == 'no':
    print('Thank you for considering our program.')