filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

message = ''
for line in lines:
    message += line.replace('Python', 'C')

print(message)
