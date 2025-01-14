while True:
    print("Type two numbers for addition (Please Enter 'q' for exit) ")

    firstnumber = input("Enter First Number: ")
    if firstnumber == 'q' :
        break
    secondnumber = input("Enter Second Number: ")
    if secondnumber == 'q' :
        break
    try :
        total = int(firstnumber) + int(secondnumber)
    except ValueError:
        print("Enter Numbers Please ! ")
    else: 
        print(f"This is the total addition of two numbers: {total}")

