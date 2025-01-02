# a polling program in which each pass through the loop
# prompts for the participant’s name and response. We’ll store the data we
# gather in a dictionary, because we want to connect each response with a
# particular user
responses = {}
#Set a flag to indicate that polling is active
polling_active =True

while polling_active:
    name=input("\n What is your name? ")
    response = input ("Which mountain would you like to climb someday? ")
    responses[name]=response
    repeat=input("Would you like to let another person respond? (yes/ no)")
    if repeat.lower() == 'no':
        polling_active = False

print("\n------- Poll Results -------------")

for name,response in responses.items():
    print(f"You are {name} and you will climb {response}")
