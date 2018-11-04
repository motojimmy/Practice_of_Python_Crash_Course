
filename = 'learning_python.txt'

with open(filename) as file_object:
    contents = file_object.read()
    print(contents.rstrip())

with open(filename) as file_object:
    contents = file_object.readline()
    print(contents.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()


message = ''
for line in lines:
    message += line.rstrip()

print(message)
