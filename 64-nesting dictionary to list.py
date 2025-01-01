alien_0={'color':'green','points': 5 }
alien_1={'color':'red','points': 6}
alien_2={'color':'orange','points': 11}

aliens=[alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)

#Creation of a fleet of 30 aliens

aliens=[]

for alien_number in range(1,31):
    new_alien={'color':'orange','points': 11, 'speed':"slow"}
    aliens.append(new_alien)

for alien in aliens[:5]:
    print(alien)
print(f'Total number of aliens : {len(aliens)}')

#make the first 3 aliens yellow color and speed medium with points 10

for alien in aliens[:3]:
    if alien['color'] == 'orange':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = "medium"
    elif alien["color"] == "yellow":
        alien['color'] = 'red'
        alien['points'] = 50
        alien['speed'] = "fast"


for alien in aliens[:5]:
    print(alien)