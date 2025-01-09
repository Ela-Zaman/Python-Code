from pathlib import Path

path = Path("one-million.txt")
content=path.read_text()
lines= content.splitlines()
pi_string =""

for line in lines:
    pi_string+=line.strip()

while True:

    birthday = input("Enter your birthday, in the form mmddyy: ")
    if birthday == "q":
        break

    if birthday in pi_string:
        print("Your birthday appears in the first 1 million digits of pi!")
    else:
        print("Your birthday does not appears in the first million digits of pi ")


