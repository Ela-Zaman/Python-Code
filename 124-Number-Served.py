class Restaurant:
    
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisune_type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"The name of the restaurant is {self.restaurant_name}\n")
        print(f"The cuisine type is {self.cuisune_type}")
    
    def open_restaurant(self):
        print("The restaurant is open")
    
    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,increment):
        self.number_served+=increment


restaurant = Restaurant("Sea Shell","Indian")

print(f"{restaurant.restaurant_name} served {restaurant.number_served} people\n")

restaurant.number_served = 10
print(f"{restaurant.restaurant_name} served {restaurant.number_served} people\n")

restaurant.set_number_served(100)
print(f"{restaurant.restaurant_name} served {restaurant.number_served} people\n")

restaurant.increment_number_served(200)

print(f"{restaurant.restaurant_name} served {restaurant.number_served} people\n")
