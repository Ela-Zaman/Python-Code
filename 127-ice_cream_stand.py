class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisune_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}\n")
        print(f"The cuisine type is {self.cuisune_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")

restaurant = Restaurant("Sea Shell","Indian")

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type,flavors):
        super().__init__( restaurant_name, cuisine_type)
        self.flavors=flavors

    def display_icecream_flavor(self):
        print("We have following flavors: ")
        for flavor in self.flavors:
            print(f"-{flavor}")
    

icecream_stand=IceCreamStand("polar","indian", ["strawberry", "vanilla", "chocolate"])

icecream_stand.display_icecream_flavor()
    
