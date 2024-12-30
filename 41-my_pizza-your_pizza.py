pizzas =["chicken", "beef", "vegetable"]
friends_pizzas=pizzas[:]

pizzas.append("cheese")
friends_pizzas.append("salami")

print("My favourite pizza's are: ")

for pizza in pizzas:
    print(pizza)

print("My friend's favourite pizza's are: ")

for pizza in friends_pizzas:
    print(pizza)

new_pizza_2=[pizza for pizza in pizzas]
friends_pizzas_2=[pizza for pizza in friends_pizzas]

print("Pizza List: \n",new_pizza_2)
print("Friend's Pizza list: \n",friends_pizzas_2)