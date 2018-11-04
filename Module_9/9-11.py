from user import Privileges
class Admin(User):
    # 用于描述管理员信息的类
    def __init__(self, first_name, last_name, gender, age):
        super(Admin, self).__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()


admin_02 = Admin('jimmy', 'fang', 'male', 34)

admin_02.privileges.show_privileges()
