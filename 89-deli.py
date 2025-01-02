sandwich_orders = ["chicken","beef","vegetable","egg" ,"chicken"]
finished_sandwiches= []

while sandwich_orders:
    order = sandwich_orders.pop()
    print(f"I made your {order} sandwich")
    finished_sandwiches.append(order)

print(f"This is the list of prepared sandwiches \n{finished_sandwiches}")