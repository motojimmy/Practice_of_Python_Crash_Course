filename = 'when you were a boy.txt'

with open(filename, 'r') as file_object:
    lines = file_object.readlines()

story_str = ''
for line in lines:
    print(line.rstrip())
    story_str += line.rstrip()

print(story_str)
print(len(story_str))
print(story_str.count('the'))

