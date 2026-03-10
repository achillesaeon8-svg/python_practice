first_number = float(input("Enter your first number: "))
second_number = float(input("Enter your second number: "))

if first_number > second_number:
    print(first_number, "is the bigger number")
elif first_number < second_number:
    print(second_number, "is the bigger number")
else:
    print("Incorrect input")