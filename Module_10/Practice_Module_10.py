# https://cn.aliyun.com/jiaocheng/516758.html
print("\n**************************************************")
print("< 10-1 >")

# filename = 'learning_python.txt'
#
# with open(filename) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())
#
# with open(filename) as file_object:
#     contents = file_object.readline()
#     print(contents.rstrip())
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
#
# message = ''
# for line in lines:
#     message += line.rstrip()
#
# print(message)
#
#
#
#
# print("\n**************************************************")
# print("< 10-2 >")
#
# filename = 'learning_python.txt'
#
# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# message = ''
# for line in lines:
#     message += line.replace('Python', 'C')
#
# print(message)
#
#
#
# print("\n**************************************************")
# print("< 10-3 >")
#
# filename = 'guest.txt'
#
# with open(filename, 'w') as file_object:
#     file_object.write( input( "Please input your username: " ) + "\n" )
# with open( filename, 'a' ) as file_object:
#     file_object.write( input( "Please input your username: " ) + "\n" )
#     file_object.write( input( "Please input your username: " ) + "\n" )
#
#
# print("\n**************************************************")
# print("< 10-4 >")
#
# # filename = 'guest_book.txt'
# #
# # username = input("Please input your username: ")
# #
# # while username.strip() == '':
# #     username = input( "Please input your username: " )
# # with open(filename, 'a') as file_object:
# #     file_object.write("User " + username + " visit the system." + "\n")
# #     print( "Hello " + username + "! Welcome to visit our system!")
# #
# #
# # print("\n**************************************************")
# # print("< 10-5 >")
# #
# # filename = 'reason.txt'
# #
# # the_reason = input("Why do you like programming? ")
# # while the_reason.strip() == '':
# #     the_reason = input( "Why do you like programming? " )
# # with open(filename, 'a') as file_object:
# #     file_object.write( the_reason + "\n" )
# #
#
# print("\n**************************************************")
# print("< 10-6 >")
#
# first_number = input("First number: ")
# second_number = input("Second number: ")
# try:
#     add = int(first_number) + int(second_number)
# except ValueError:
#     print("You must enter digits!!!")
# else:
#     print(add)
#
#
# print("\n**************************************************")
# print("< 10-7 >")
#
# print("Please enter two digits, I will add the two numbers.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("First number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         add = int(first_number) + int(second_number)
#     except ValueError:
#         print("You must enter digits!!!\n")
#     else:
#         print(add)

print("\n**************************************************")
print("< 10-8 >")

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


print("\n**************************************************")
print("< 10-9 >")

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

print("\n**************************************************")
print("< 10-10 >")

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


print("\n**************************************************")
print("< 10-11 >")

import json

number = 19920821

filename = 'my_number.json'
with open(filename, 'w') as file_object:
    json.dump(number, file_object)
    print("The number has been stored in file " + filename)

with open(filename) as file_object:
    my_number = json.load(file_object)
    print( "I know your favorite number! It's " + str(my_number) + ".")


print("\n**************************************************")
print("< 10-12 >")

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


print("\n**************************************************")
print("< 10-13 >")

import json

def get_stored_username():
    #如果存储了用户名，就提取它
    filename = 'username.json'
    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    username = get_stored_username()
    if username:
        print("Now the username is " + username + ".")
        check_module = input("Is this your username? Yes or No ")
        if check_module.lower() == 'yes':
            print("Welcome back " + username + ".")
        else:
            username = get_new_username()
            print("We'll remember you when you come back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()

