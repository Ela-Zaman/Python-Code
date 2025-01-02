prompt="Enter a series of pizza toppings"
prompt += "\n (Enter quit value to exit)\n"


while True:
    message = input(prompt)
    if message == "quit":
        break
    else:
        print(f"We all add {message} topping to your pizza\n")
    
