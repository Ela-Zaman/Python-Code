
print("Enter Two Number: ")
firstnumber = input("First Number: ")
secondnumber = input("Second Number: ")

try:
    total = int(firstnumber) + int(secondnumber)
except ValueError:
    print("Please Provide Numbers")
else:
    print(f"This is the addition of two numbers: ", total)

