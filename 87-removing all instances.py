pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')


print(pets)

items = ['bottle','mobile','calculator','bottle', 'charger', 'laptop']
for item in items:
    if item == "bottle" :
        items.remove("bottle")

print(items) 
