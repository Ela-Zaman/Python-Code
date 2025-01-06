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

print(f"Restaurant name: {restaurant.restaurant_name}\n")
print(f"Cuisine type: {restaurant.cuisune_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

#Three Restaurant - three restaurant()

restaurant_1 = Restaurant("Skyway", "Chinese")
restaurant_1.describe_restaurant()
restaurant_2 = Restaurant("KFC", "American")
restaurant_2.describe_restaurant()
restaurant_3 = Restaurant("CP","Local")
restaurant_3.describe_restaurant()