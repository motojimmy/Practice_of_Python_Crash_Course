import json

number = 19920821

filename = 'my_number.json'
with open(filename, 'w') as file_object:
    json.dump(number, file_object)
    print("The number has been stored in file " + filename)

with open(filename) as file_object:
    my_number = json.load(file_object)
    print( "I know your favorite number! It's " + str(my_number) + ".")

