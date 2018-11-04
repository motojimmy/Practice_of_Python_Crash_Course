filename = 'guest.txt'

with open(filename, 'w') as file_object:
    file_object.write( input( "Please input your username: " ) + "\n" )
with open( filename, 'a' ) as file_object:
    file_object.write( input( "Please input your username: " ) + "\n" )
    file_object.write( input( "Please input your username: " ) + "\n" )

