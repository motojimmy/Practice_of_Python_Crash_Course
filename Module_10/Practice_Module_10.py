# https://cn.aliyun.com/jiaocheng/516758.html
print("\n**************************************************")
print("< 10-1 >")

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




print("\n**************************************************")
print("< 10-2 >")

filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

message = ''
for line in lines:
    message += line.replace('Python', 'C')

print(message)



print("\n**************************************************")
print("< 10-3 >")

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write( input( "Please input your username: " ) + "\n" )
with open( filename, 'a' ) as file_object:
    file_object.write( input( "Please input your username: " ) + "\n" )
    file_object.write( input( "Please input your username: " ) + "\n" )


print("\n**************************************************")
print("< 10-4 >")

# filename = 'guest_book.txt'
#
# username = input("Please input your username: ")
#
# while username.strip() == '':
#     username = input( "Please input your username: " )
# with open(filename, 'a') as file_object:
#     file_object.write("User " + username + " visit the system." + "\n")
#     print( "Hello " + username + "! Welcome to visit our system!")
#
#
# print("\n**************************************************")
# print("< 10-5 >")
#
# filename = 'reason.txt'
#
# the_reason = input("Why do you like programming? ")
# while the_reason.strip() == '':
#     the_reason = input( "Why do you like programming? " )
# with open(filename, 'a') as file_object:
#     file_object.write( the_reason + "\n" )
#

print("\n**************************************************")
print("< 10-6 >")

first_number = input("First number: ")
second_number = input("Second number: ")
try:
    add = int(first_number) + int(second_number)
except ValueError:
    print("You must enter digits!!!")
else:
    print(add)


print("\n**************************************************")
print("< 10-7 >")

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
