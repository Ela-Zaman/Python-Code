pizza={
    'crust': 'thick',
    'toppings':['mushrooms','extra cheese']
}

print(f"You ordered a {pizza['crust']} pizza with following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

