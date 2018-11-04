first_number = input("First number: ")
second_number = input("Second number: ")
try:
    add = int(first_number) + int(second_number)
except ValueError:
    print("You must enter digits!!!")
else:
    print(add)