# A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop because Python will have trouble keeping track of
# the items in the list. To modify a list as you work through it, use a while loop.
# Using while loops with lists and dictionaries allows you to collect, store, and
# organize lots of input to examine and report on later.

print("Moving item from one list to other")

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users=[]

while unconfirmed_users:
    #list.pop()=> extract the last value of the list.
    current_user=unconfirmed_users.pop()
    print(f"Verifying User {current_user.title()}")
    confirmed_users.append(current_user)

#Display all confirmed users.

print("\n The following users have been confirmed:")
for confirmed in confirmed_users:
    print(confirmed.title())