
dream_vacations={}

poll = True 

while poll:
    name = input("What is your name ? \n")
    vacation = input("If you could visit one place in the world,\
                  where would you go ? \n")
    
    dream_vacations[name] = vacation
    
    repeat=input("Do you like to add another person: \n",)
    if repeat.lower() == "no":
        poll = False
    
for name, vacation in dream_vacations.items():
    print(f"{name} is going to {vacation}")



