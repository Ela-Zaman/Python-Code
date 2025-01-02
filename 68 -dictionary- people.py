person_1={
    "first_name" : "Razia Zaman",
    "last_name": "Ela",
    "age" : 20,
    "city" :"dhaka",
}

person_2={
    "first_name" : "Toha ",
    "last_name": "Ahmed",
    "age" : 15,
    "city" :"uttara",
}
person_3={
    "first_name" : "Doha",
    "last_name": "Ahmed",
    "age" : 18,
    "city" :"london",
}

persons=[person_1,person_2,person_3]

for person in persons:
    print(f"Information of the person:\n")
    for key,value in person.items():
       
        print(f"{key}: {value}")

