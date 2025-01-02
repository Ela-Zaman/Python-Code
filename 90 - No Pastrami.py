sandwich_orders = ["chicken","pastrami","beef","pastrami","vegetable",\
                   "egg" ,"chicken","pastrami"]

finished_sandwiches=[]

print("the deli has run out of pastrami")

while sandwich_orders:
    item=sandwich_orders.pop()
    if item != "pastrami" :
        finished_sandwiches.append(item)

print(f"Available sandwiches: \n {finished_sandwiches}")

