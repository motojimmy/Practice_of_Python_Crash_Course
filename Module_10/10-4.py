filename = 'guest_book.txt'

username = input("Please input your username: ")

while username.strip() == '':
    username = input( "Please input your username: " )
with open(filename, 'a') as file_object:
    file_object.write("User " + username + " visit the system." + "\n")
    print( "Hello " + username + "! Welcome to visit our system!")