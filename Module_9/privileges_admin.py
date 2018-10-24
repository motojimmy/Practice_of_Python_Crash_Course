
from user_01 import User

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
