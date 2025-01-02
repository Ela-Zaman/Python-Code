prompt= "Enter a message : I will repeat\n"
prompt += "\n enter quit to end this program"

active= True
while active:
    message= (input(prompt))
    if message == "quit" :
        active = False
    else:
        print(message)

