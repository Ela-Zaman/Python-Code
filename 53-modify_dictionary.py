alien_0={"color":"red"}
print(alien_0)

alien_0['color'] = "orange"
print("modify colors: ",alien_0)

print("")
alien_0 ={"x_position":0,"y_position": 25, 'speed':'medium'}
print(f"Original position: {alien_0['x_position']}")
print(f"Moving the Alien to right")

if alien_0["speed"] == "slow":
    x_increment= 2
elif alien_0["speed"] == "medium":
    x_increment = 4
elif alien_0["speed"] == "fast":
    x_increment = 6

alien_0["x_position"]=alien_0["x_position"]+x_increment

print(f"position of the alien : {alien_0["x_position"]}")

#modifying value

del alien_0["speed"]
print(alien_0)

#a dictionary of similiar object

favourite_language={"jen": "python","sarah":"c","edward":"rust", \
                    "phil":"python"}

favourite_language={
    "jen":"pyhon",
    "abu":"c",
    }

language= favourite_language["abu"].title()
print(f"Sarah's favourite language is : {language}")

#get() method 

alien_0 ={'color': "green", "speed":"slow"}
point_value=alien_0.get("point","No value exist")
print(point_value)

point_value=alien_0.get("point")
print(point_value)

