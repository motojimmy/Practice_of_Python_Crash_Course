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


r
restaurant_2 = Restaurant('Jing Wei Zhai', 'Chinese Food')
restaurant_3 = Restaurant('BurgKing', 'Western Fast Food')
restaurant_4 = Restaurant('Mcdonald', 'Western Fast Food')

restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()
restaurant_4.describe_restaurant()
