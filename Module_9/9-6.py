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

