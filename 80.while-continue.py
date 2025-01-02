#Consider a loop that counts from 1 to 10 but prints only the odd numbers in
# in the range
num = 0
print ("Here's the odd number between 1 to 10\n")
while num < 10 :
    num += 1
    if num % 2 == 0:
        continue
    print(num)
    