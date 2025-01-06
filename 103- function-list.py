def great_users(names):
    for name in names:
        print(f"Hello {name.title()}, Welcome !")

usernames=['hannah', 'ty', 'margot']
great_users(usernames)

# Consider a company that creates 3D printed models of designs that
# users submit. Designs that need to be printed are stored in a list, and after
# being printed they’re moved to a separate list
unprinted_designs=['circle',"rectangle","triangle", "pentagone"]
printed_designs=[]

while unprinted_designs:
    design = unprinted_designs.pop()
    printed_designs.append(design)
    print(f"Now printing {design}")

print(" \n The following models have been printed : ")
for printed_design in printed_designs:
    print(printed_design)
