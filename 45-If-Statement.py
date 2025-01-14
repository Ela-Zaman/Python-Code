cars=['audi','bmw','toyota','nissan']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

requested_topping='mashrooms'

if requested_topping != 'anchovies' :
    print("Hold the anchovies")

#checking a value is in list

requested_toppings = ['mushrooms', 'onions' , 'pineapple']


if 'mushrooms' in requested_toppings:
    print("wow")
else:
    print("sorry")

#checking a value is not in list

if "salami"  not in requested_toppings:
    print("Wow, ovro hates you")
else:
    print("I don't care")
#boolean expressions

game_active = True
game_deactive = False
