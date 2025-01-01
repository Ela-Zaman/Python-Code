#[] : square brackets - list
#{} : braces      -dictionary
#() : parenthesis -tuple
#dictionary:  a series of key value pairs
alien_0={'color':'red','points':5}

print(alien_0['color'])
print(alien_0['points'])
new_points =alien_0["points"]
print(f"You just earned {new_points} points!")

alien_0['x_position']= 0
alien_0['y_positiom'] = 25

print(alien_0)


#starting with an empty Dictionary
alien_0={}

alien_0['color'] ="red"
alien_0['points'] = 0

print(f"print alien's character {alien_0}")