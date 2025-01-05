def make_shirt(size,message):
    print(f"The size of the shirt {size} and {message} should be printed")

make_shirt("XL", "Eat, Pray, Love")
#use a backslash (\) to escape the double quotation marks:
make_shirt(size="M", message="\"Pretty's on the inside\"")

def make_shirt_2(size="large", message = "I Love Python"):
    
    print(f"The shirt is in {size} size and this Message\"{message}\"should be\
           printed".strip())
    
make_shirt_2()
make_shirt_2("small","Are you pretty ?")