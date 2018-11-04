filename = 'reason.txt'

the_reason = input("Why do you like programming? ")
while the_reason.strip() == '':
    the_reason = input( "Why do you like programming? " )
with open(filename, 'a') as file_object:
    file_object.write( the_reason + "\n" )