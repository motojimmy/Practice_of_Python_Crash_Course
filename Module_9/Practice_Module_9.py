
print("\n**************************************************")
print("< 9-1 >")


class Restaurant:
    # 用于描述餐馆的类
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print("The name of this restaurant is " + self.name.title() + '.')
        print("The type of this restaurant is " + self.type.title() + '.')

    def open_restaurant(self):
        print("The restaurant is open now.")


restaurant_1 = Restaurant('Da Ya Li', 'Chinese Food')

restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()


print("\n**************************************************")
print("< 9-2 >")

restaurant_2 = Restaurant('Jing Wei Zhai', 'Chinese Food')
restaurant_3 = Restaurant('BurgKing', 'Western Fast Food')
restaurant_4 = Restaurant('Mcdonald', 'Western Fast Food')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()


print("\n**************************************************")
print("< 9-3 >")


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


print("\n**************************************************")
print("< 9-4 >")


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        print("The name of this restaurant is " + self.name.title() + '.')
        print("The type of this restaurant is " + self.type.title() + '.')

    def open_restaurant(self):
        print("The restaurant is open now.")

    def set_number_served(self, number_served):
        self.number_served = number_served
        print("There are " + str(self.number_served) +
              " people have been served in this restaurant.")

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


restaurant_1 = Restaurant('Da Ya Li', 'Chinese Food')

restaurant_1.set_number_served(100)
restaurant_1.increment_number_served(200)

print("There are " + str(restaurant_1.number_served) + " people have been served in this restaurant.")


print("\n**************************************************")
print("< 9-5 >")


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


user_1 = User('jian', 'fang', 'male', 34)

user_1.describe_user()
user_1.greet_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
print(user_1.login_attempts)

user_1.reset_login_attempts()
print(user_1.login_attempts)




print("\n**************************************************")
print("< 9-6 >")


class IceCreamStand(Restaurant):
    #  用于描述冰激凌甜品店的子类
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['super-sweet', 'medium-sweet',
                          'peppermint', 'chacolate',
                          'strawberry', 'blueberry']


    def your_choices(self):
        print("You can select following flavors:\n")
        for flavor in self.flavors:
            print('- ' + flavor.title())
        print("\nEnjoy your meal! ")

ice_creams_01 =  IceCreamStand('Burgjing', 'Western Fast Food')

ice_creams_01.your_choices()
ice_creams_01.flavors.append('stinky tofu')

ice_creams_01.your_choices()



print("\n**************************************************")
print("< 9-7 >")

class Admin(User):
    # 用于描述管理员信息的类
    def __init__(self, first_name, last_name, gender, age):
        super(Admin, self).__init__(first_name, last_name, gender, age)
        self.privileges = ["can add post", "can delete post",
                           "can ban user"]

    def show_privileges(self):
        print("You have following privileges:\n")
        for privilege in self.privileges:
            print('- ' + privilege.title())

admin_01 = Admin('Jimmy', 'Fang', 'Male', 34)

admin_01.show_privileges()


print("\n**************************************************")
print("< 9-8 >")

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



print("\n**************************************************")
print("< 9-9 >")


class Car():
# 用于描述汽车的类
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year + ' ' + self.make + ' ' + self.model)
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
# 用于描述电池的类
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) +
              " -kWh battery.")

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85



class ElectricCar(Car):
# 用于描述电动汽车的类
    def __init__(self,make, model, year):
        super(ElectricCar, self).__init__(make, model, year)
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.battery.battery_size)
my_tesla.battery.get_range()

my_tesla.battery.upgrade_battery()
print(my_tesla.battery.battery_size)
my_tesla.battery.get_range()



print("\n**************************************************")
print("< 9-10 >")

from restaurant import Restaurant

new_restaurant_01 = Restaurant('jing wei zhai', 'chinese food')
new_restaurant_01.describe_restaurant()



print("\n**************************************************")
print("< 9-11 >")

from user import Privileges

admin_02 = Admin('jimmy', 'fang', 'male', 34)

admin_02.privileges.show_privileges()



print("\n**************************************************")
print("< 9-12 >")

from privileges_admin import Admin, Privileges

admin_03 = Admin('jimmy', 'fang', 'male', 34)

admin_03.privileges.show_privileges()



print("\n**************************************************")
print("< 9-13 >")

from collections import OrderedDict

dic_01 = OrderedDict()

dic_01['print'] = 'print output value on screen'
dic_01['exit'] = 'logout'
dic_01['remove']= 'remove the data'

for key, value in dic_01.items():
    print(key + ": " + value)


print("\n**************************************************")
print("< 9-14 >")

from random import randint
class Die():
# 用于模拟掷骰子的类,定义了 骰子面数 和 掷骰子次数
    def __init__(self, sides, times):
        self.sides = sides
        self.times = times

    def roll_die(self):
        time = range(1, self.times + 1)
        for n in time:
            x = randint(1, self.sides)
            print(x)
        print("\n")

shai_zi_01 = Die(6, 10)

shai_zi_01.roll_die()



shai_zi_02 = Die(10, 10)

shai_zi_02.roll_die()


shai_zi_03 = Die(20, 10)

shai_zi_03.roll_die()



print("\n**************************************************")
print("< 9-15 >")

print('Visit the website http://pymotw.com and find more '
      'information about the Standard Library. ')
