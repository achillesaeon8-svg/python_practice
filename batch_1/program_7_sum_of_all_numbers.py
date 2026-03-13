chosen_numbers = []
print("Enter 10 numbers: ")

for i in range(9):
    numbers = float(input("Enter {i+1} numbers: "))
    chosen_numbers.append(numbers)
    all_numbers_sum = chosen_numbers

print("The sum of all 10 numbers are", all_numbers_sum)