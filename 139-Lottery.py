from random import choice
new_list=[1,2,'a',3,4,'b',5,6,'c',7,8,'d',9,'e',10,]

lottery=""

for item in range(4):
    lottery+=str(choice(new_list))

print(f"Any tickets matching this values {lottery} wins a price")

