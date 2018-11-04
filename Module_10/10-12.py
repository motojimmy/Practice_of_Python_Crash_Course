import json

filename = 'new_number.json'

try:
    with open(filename) as file_object:
        new_number = json.load(file_object)
except FileNotFoundError:
    new_number = input("Please input your favorite number: ")
    print(new_number)
    print(type(new_number))
    with open(filename, 'w') as file_object:
        json.dump(new_number, file_object)
        print("New number has been stored in file " + filename + ".")

else:
    print(new_number)