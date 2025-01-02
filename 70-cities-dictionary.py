cities={
    "uttara":{"county":"Bangladesh",
             "population":"10 cr",
             "fact":"developped"},
    "dhaka":{"county":"Bangladesh",
             "population":"15 cr",
             "fact":"capital"},
    "gazipur":{"county":"Bangladesh",
             "population":"5 cr",
             "fact":"Bad road"},
            }

# for name,info in cities.items():
#     print(f"name of the city : {name}")
#     for key,value in info.items():
#         print(f"\t{key} : {value}")

cities['barishal']= {"county":"Bangladesh",
             "population":"5 cr",
             "fact":"Bad ",}
for name,info in cities.items():
    print(f"name of the city : {name}")
    for key,value in info.items():
        print(f"\t{key} : {value}")
      