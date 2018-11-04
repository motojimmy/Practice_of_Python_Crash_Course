filename_01 = 'catss.txt'
filename_02 = 'dogs.txt'

try:
    with open(filename_01) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    message = ("Sorry, the file " + filename_01 + " does not exist. ")
    print(message)
else:
    for line in lines:
            print(line)
try:
    with open(filename_02) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    message = ("Sorry, the file " + filename_02 + " does not exist. ")
    print(message)
else:
    for line in lines:
        print(line)