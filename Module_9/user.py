class User:

    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("- User name: " + self.last_name.title()
              + ' ' + self.first_name.title())
        print("- User gender: " + self.gender.title())
        print("- User age: " + str(self.age))

    def greet_user(self):
        print(self.last_name + self.first_name +
              ", thanks for your kindly interest! ")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, gender, age):
        super(Admin, self).__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()



class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post",
                           "can ban user"]

    def show_privileges(self):
        print("You have following privileges:\n")
        for privilege in self.privileges:
            print('- ' + privilege.title())

