filename_01 = 'cats.txt'
filename_02 = 'dogs.txt'

try:
    with open(filename_01) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
            print(line)
try:
    with open(filename_02) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line)