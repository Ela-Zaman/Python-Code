Rivers={
    'nile' : 'egypt',
    'padma': 'bangladesh',
    'ganga': 'india',
}

for key,value in Rivers.items():
    print(f"The {key} runs through {value}")

for name in Rivers.keys():
    print(name)
    
for country in Rivers.values():
    print(country)