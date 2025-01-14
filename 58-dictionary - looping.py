user_0= {
    'username' : "efermi",
    'first':"enrico",
    'last' : "fermi"
}
for key,value in user_0.items():
    print(f"\nKey: {key}")
    print(f"\nValue:{value}")

#favourite Language - dictionary
favourite_languages={"jen": "python","sarah":"c","edward":"rust", \
                    "phil":"python"}

for name,language in favourite_languages.items():
    print(f"{name.title()}'s favourite language is {language.title()}")

print("Print only the value in the dictionary\n")

for name in favourite_languages.keys():
    print(f"{name.title()} is a key in the dictionary ")

#It works the same
for name in favourite_languages:
    print(f"{name.title()} is a key in the dictionary ")


print("Loop through dictionary to check condition")
friends=["sarah", "phil"]

for name in favourite_languages.keys():
    print(f"Hi, {name}")
    if name in friends:
        print(f"\tHi, {name} , I see you like {favourite_languages[name]}")

if "erin" not in favourite_languages.keys():
    print("Hey,erin take our poll!")

