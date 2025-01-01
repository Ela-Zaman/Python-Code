favourite_languages={
    'jen' : ['python', 'rust'],
    'sarah' : ['c'],
    'edward': ['rust','go'],
    'phil' : ['python', 'haskel'],
}

for name,languages in favourite_languages.items():
    print(f"{name.title()}'s favourite languages are : ")
    for language in languages:
        print(f"\t{language.title()}")
