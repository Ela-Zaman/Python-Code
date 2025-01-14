# : A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# of their movie ticket.



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
    