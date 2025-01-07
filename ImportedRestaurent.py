class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisune_type = cuisine_type
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}\n")
        print(f"The cuisine type is {self.cuisune_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")
