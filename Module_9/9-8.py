
class Privileges:
    # 用于描述权限的类
    def __init__(self):
        self.privileges = ["can add post", "can delete post",
                           "can ban user"]

    def show_privileges(self):
        print("You have following privileges:\n")
        for privilege in self.privileges:
            print('- ' + privilege.title())

class Admin(User):
    # 用于描述管理员信息的类
    def __init__(self, first_name, last_name, gender, age):
        super(Admin, self).__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()


admin_01 = Admin('Jimmy', 'Fang', 'Male', 34)

admin_01.privileges.show_privileges()

