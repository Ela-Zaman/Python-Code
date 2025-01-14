from name_function import get_formatted_name



print("Enter 'q' at any time to quit. ")
while True:
    first = input("\n Please give me a first name: ")
    if first == 'q' :
        break
    last = input("Please give me a lastname: ")
    if last == 'q' : 
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\t Neatly formatted name: {formatted_name}")
