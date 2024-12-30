user_names=[]
if user_names:
    for user_name in user_names:
        if user_name == "admin":
            print(f"Hello {user_name},would you like to see a status report?")
        else:
            print(f"Hello {user_name},thank you for logging in again ")
else:
    print("We need to find some users!")


print("Checking Username: /n")

current_users=["ela","Doha","Toha","Enam","Lucky"]
new_current_users=[current_user.lower() for current_user in current_users]
new_users=["nora","prana","jaana","Ela","Doha"]

for new_user in new_users:
    if new_user.lower() in new_current_users:
        print(f"{new_user}, you need to enter a new username")
    else:
        print(f"{new_user} username is available")


