motorcycles=['honda','ducati','suzuki']

#permanently delete item from the list
del motorcycles[0]
print(motorcycles)

#remove the last item from the list and we can store it in a variables

popped_motorcycle=motorcycles.pop()

print(popped_motorcycle)
print(motorcycles)
#remove a value from the list, but don't know position
motorcycles= ['honda','ducati','suzuki']
print(motorcycles.remove('suzuki'))
print(motorcycles)

#work with removed item

expensive='ducati'
motorcycles.remove(expensive)


print(f"{expensive} is too expensive for me" )
print(motorcycles)

#remove() delete only the first occurances of the value in the list