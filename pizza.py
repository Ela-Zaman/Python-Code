#using descreptive names for my function
def make_pizza(size, *toppings):
    print(f"\n Making a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"-{topping}")




