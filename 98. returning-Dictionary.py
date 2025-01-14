def build_person(first_name,last_name):
    """Return a dictionary of information about a person"""
    person={'first': first_name,
            'last': last_name}
    return person

musician = build_person("Razia", "Zaman")
print(musician)

def build_person(first_name, last_name, age = None):
    person={"first": first_name,
            "last_name": last_name}
    if age:
        person["age"]=age
    return person

person_1 = build_person("Razia", "Ela", 27)
print(person_1)
person_2 = build_person("Doha", "Ahmed")
print(person_2)   


    