dimensions=(200,300)

print(dimensions[0])
print(dimensions[1])

# we cannot change items in a tuple, it will raise error
#dimensions[0] = 1000

# dimensions[0] = 150
# print(dimensions)

#keyboard shortcut for multiline comments : ctrl + /
#define a tuple in one element
my_t=(3,)

print(my_t)

#looping through All Values in a Tuple

dimentions=(200,50)
print("Original dimensions:")

for dimention in dimentions:
    print(dimention)

# we cannot change items of tuple but we can redefine the tuple

dimentions=(400,0)
print("Original dimensions:\n",dimentions)

