# sort alphabetically

cars=['bmw','marcidis','audi','toyota']
cars.sort()

print(cars)

#sort reverse alphabetical 
cars.sort(reverse=True)
print(cars)

#temporarily sorted()

print("Here the original list")
print(cars)

print("\nHere the sorted list")
print(sorted(cars))

print("\n Here the original list again")
print(cars)

#reverse() : reverses the order of the list permanently

cars.reverse()
print(cars)
#Number of item in the list
print(len(cars))


