requested_toppings=['mashrooms','green peppers','extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == "green peppers":
        print("Sorry we are out of green peppers")
    else:
        print(f"Adding {requested_topping} to your pizza")
print("Finished . Enjoy your pizza")

#checking the list is not empty

requested_toppings=[]

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"We are Adding {requested_topping} to your pizza")
else:
    print("Are you sure you want plain pizza ?")


    