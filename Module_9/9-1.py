
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