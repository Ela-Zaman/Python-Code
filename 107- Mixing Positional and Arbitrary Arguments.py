def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print(f"\nMaking a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print(f"Topping: {topping}\n")
make_pizza(12,"mushroom", "chicken","beef")
make_pizza(6,"egg", "mushroom")