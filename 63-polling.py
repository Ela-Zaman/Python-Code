favourite_languages={"jen": "python","sarah":"c","edward":"rust", \
                    "phil":"python"}


people=["ela","doha","phil","sarah"]



for name in people:
    if name in favourite_languages.keys():
        print(f"{name} Thank you for taking the poll")
    elif name not in favourite_languages.keys():
        print(f'{name}, you are invited to taking the poll')