def describe_pet(animal_type, pet_name):
    print(f"\n I have a {animal_type}")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster','harry')
describe_pet('dog','Willie')

#Keyword Argument
#if we use keyword Argument the position of the values of the arguments do not 
#varry

describe_pet(animal_type="cat", pet_name="tommy")
describe_pet(pet_name="jerry", animal_type="mouse")

#default value

def describe_pet(animal_type, pet_name = "jerry"):

    {
        print(f"I like the pet {animal_type} with the name {pet_name}")


    }
describe_pet("mouse")
describe_pet("mouse", "misti")