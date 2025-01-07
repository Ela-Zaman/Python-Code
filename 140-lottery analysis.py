from random import choice
new_list=[1,2,'a',3,4,'b',5,6,'c',7,8,'d',9,'e',10,]

lottery=""

my_ticket=['a','b', 1 , 2]
ticket = ""

for item in my_ticket:
    ticket+=str(item)

print(f"My Ticket: {ticket}")

count=0

while True:
    
    lottery=""

    for item in range(4):
        lottery+=str(choice(new_list))
    
    print(lottery)

    if ticket != lottery :
        count=count+1
    else:
        print(f"The loop had to run {count} times to give you winning ticket")
        break

