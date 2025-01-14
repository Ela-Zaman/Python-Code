from pathlib import Path
import json

def print_favourite_number():

    path= Path("favourite_number.json")
    contents = path.read_text()
    if contents:
        favourite_number = json.loads(contents)
        print(f"Your Favourite Number: {favourite_number}")
    else:
        get_favourite_number()


def get_favourite_number():
    favourite_number = input("What is your favourite number ? ")
    path = Path('favourite_number.json')
    contents = json.dumps(favourite_number)
    path.write_text(contents)
    print(f"Your Favourite Number: {favourite_number}")

print_favourite_number()


