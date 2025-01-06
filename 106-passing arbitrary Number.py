
# Here's the added *toppings save all the arguments as tuple 
def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
    print("Printing the number of toppings listed")
    for topping in toppings:
        print(f'Adding: {topping}\n')


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')