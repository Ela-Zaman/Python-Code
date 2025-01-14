
my_foods=['pizza','falafel', 'carrot cake']
#copy list
friend_foods =my_foods[:]
#This doesn't work
#friend_foods =my_food - Here both variables point to the same list
print("My favourite foods: ",my_foods)
print("My friend's favourite food: ",friend_foods)

my_foods.append('Korala')
friend_foods.append('Ice Cream')

print("My favourite foods: ",my_foods)
print("My friend's favourite food: ",friend_foods)


