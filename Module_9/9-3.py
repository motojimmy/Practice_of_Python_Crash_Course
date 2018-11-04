class User:
    # 用于描述用户的类
    def __init__(self, first_name, last_name, gender, age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        print("- User name: " + self.last_name.title()
              + ' ' + self.first_name.title())
        print("- User gender: " + self.gender.title())
        print("- User age: " + str(self.age))

    def greet_user(self):
        print(self.last_name + self.first_name +
              ", thanks for your kindly interest! ")


user_1 = User('jian', 'fang', 'male', 34)

user_1.describe_user()
user_1.greet_user()
