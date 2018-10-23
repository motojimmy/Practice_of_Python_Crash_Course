
print("\n**************************************************")
print("< 9-1 >")


class Restaurant:

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

