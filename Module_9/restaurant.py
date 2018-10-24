
class Restaurant:
    """一个可用于表示餐馆的类"""
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 10

    def describe_restaurant(self):
        print( "The name of this restaurant is " + self.name.title() + '.' )
        print( "The type of this restaurant is " + self.type.title() + '.' )

    def open_restaurant(self):
        print( "The restaurant is open now." )

    def set_number_served(self, number_served):
        self.number_served = number_served
        print( "There are " + str( self.number_served ) +
               " people have been served in this restaurant." )

    def increment_number_served(self, increment_number):
        self.number_served += increment_number


