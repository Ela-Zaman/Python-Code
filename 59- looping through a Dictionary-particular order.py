#favourite Language - dictionary
favourite_languages={"jen": "python","sarah":"c","edward":"rust", \
                    "phil":"python"}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll")



favourite_numbers={
    1:"ela",
    50: "toha",
    30: "doha",
    20: "lucky"}

for name in sorted(favourite_languages.keys()):
    print(f"{name.title()}, Thank you for taking the poll")

print("Values in dictionary: ")

for language in favourite_languages.values():
    print(f'Languages: \n{language.title()}')

#We do not want print duplicate values
print("We have following languages in our list: ")
for language in set(favourite_languages.values()):
    print(f"{language.title()}")

