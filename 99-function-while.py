def get_formatted_name(first_name,last_name):
    """Return a full name, neatly formatted"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

#This is an infinite loop!

while True:
    print("\n Please tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First Name: ")
    if f_name =='q':
        break
    l_name = input("Last Name: ")
    if l_name =='q':
        break

    formatted_name=get_formatted_name(f_name, l_name)
    print(f"\n Hello, {formatted_name}")
