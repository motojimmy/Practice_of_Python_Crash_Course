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