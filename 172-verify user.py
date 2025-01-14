import json
from pathlib import Path
def create_user_dictionary():
    user={}
    user['username'] = input("What is your Name ? ")
    user['age'] = input("What is your age ? ")
    user['BG'] = input("What is your BloodGroup? ")
    path = Path("user.json")
    contents= json.dumps(user)
    path.write_text(contents)

def read_user_information():
    path= Path("user.json")
    contents=path.read_text()
    user=json.loads(contents)
    username = input("What is your name? ")
    if user['username'] != username:
        print("Welcome New User: ")
        create_user_dictionary()
        read_user_information()
    else:
        for key, value in user.items():
            print(f"The {key} of the User: {value}")


read_user_information()