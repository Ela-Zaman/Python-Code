
age = input("Enter your age")

while age != "quit":
    age=int(age)
    if age < 3:
        print("The ticket is free")
        age = "quit"
    elif age >= 3 and age <= 12 :
        print("The ticket is 10$ \n")
        age = "quit"
    elif age > 12:
        print("The ticket is 15$\n")
        age = "quit"

active = True
prompt=" Enter your age: \n"
prompt+=" Type quit to terminate the program: \n"

while active:
    age = input(prompt)
    if age == "quit":
        active = False
    else:
        age = int(age)

        if age < 3:
            print("The ticket is free")
            active = False
        elif age >= 3 and age <= 12 :
            print("The ticket is 10$ \n")
            active = False
        elif age > 12:
            print("The ticket is 15$\n")
            active = False

age = input("Hello Enter age : ") 
while True :
    if age == "quit":
        break
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free")
            break
        elif age >= 3 and age <= 12 :
            print("The ticket is 10$ \n")
            break
        elif age > 12:
            break


