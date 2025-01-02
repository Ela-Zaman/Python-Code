while True:
    age=input("What is your age: \n (Enter quit to cancel)")
    if age == "quit":
        break
    else:
        age=int(age)
    if age < 3 :
        print("The ticket is free\n")
    elif age >=3 and age <= 12 :
        print("The ticket is 10$:\n")
    elif age > 12 :
        print("The ticket is 15$:\n")
    