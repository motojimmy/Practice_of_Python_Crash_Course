print("Please enter two digits, I will add the two numbers.")
print("Enter 'q' to quit.")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    try:
        add = int(first_number) + int(second_number)
    except ValueError:
        print("You must enter digits!!!\n")
    else:
        print(add)