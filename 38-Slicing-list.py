players=["Ela", "Doha" ,"Toha", "Enam", "Lucky"]

slice_1=players[0:3]
print("First Slice : ",slice_1)

slice_2=players[1:3]
print("Second Slice : ",slice_2)

slice_3= players[:4]
print("Third Slice: ",slice_3)

slice_4=players[2:]
print("Fourth Slice: ",slice_4)

slice_5=players[-3:]
print("Fifth Slice: ,",slice_5)

#looping through the list
num=[1,2,3,4,5,6,7,8,9,10]
print("We are looping through slices")
for num in num[:2]:
    print(num)



