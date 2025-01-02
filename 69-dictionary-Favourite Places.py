favourite_places={
    "ela":["beach","mountain", "abroad"],
    "doha":["river", "forest","space"],
    "toha":["home","resort","virtual_space"]
}


for key,value in favourite_places.items():
    print(f"{key}'s favourite places\n")
    for n in value:
        print(f"\t {n}")