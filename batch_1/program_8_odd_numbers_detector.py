first_number = int(input("Enter a number: "))

if first_number % 2 == 1:
    print(first_number, "is an odd number")

elif first_number % 2 == 0:
    print(first_number, "is not an odd number")

else:
    print("Invalid input. Please try again.")