class Restauraunt:

    def __init__(self,restauraunt_name,cuisine_type):
        self.restauraunt_name = restauraunt_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restauraunt(self):
        print(f'Name of establishment: {self.restauraunt_name}, Food: {self.cuisine_type}')

    def open_restauraunt(self):
        print(f'{self.restauraunt_name} is now open for business!')

    def set_number_served(self,served):
        self.number_served = served
        print(f'The number of people served is: {self.number_served}')

    def increment_number_served(self, increment_served):
        
        self.number_served += increment_served
        print(f'Number of people served has increased by {increment_served} to {self.number_served}')


class IceCreamStand(Restauraunt):

    def __init__(self,restauraunt_name,cuisine_type,flavours):
        super().__init__(restauraunt_name,cuisine_type)
        self.flavours = flavours

    def desc_flavours(self):
        print(f'Flavours are: {self.flavours}')

morellis = IceCreamStand("Morellis", "Icecream", "Choc, vinilla")

morellis.describe_restauraunt()

morellis.desc_flavours()