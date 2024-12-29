people_list=["Ela","Doha","Toha","Itty"]

print(f'{people_list[0]} you are invited')
print(f'{people_list[1]} you are invited')
print(f'{people_list[2]} you are invited')
print(f'{people_list[3]} you are invited')
print(f'{people_list[3]} cannot make it')
people_list[3]="Nirob"

print(f'{people_list[0]} you are invited')
print(f'{people_list[1]} you are invited')
print(f'{people_list[2]} you are invited')
print(f'{people_list[3]} you are invited')

print("I found a bigger table")
people_list.insert(0,'mina')
people_list.insert(3,'tina')
people_list.append('ritu')

print(f'{people_list[0]} you are invited')
print(f'{people_list[1]} you are invited')
print(f'{people_list[2]} you are invited')
print(f'{people_list[3]} you are invited')
print(f'{people_list[4]} you are invited')
print(f'{people_list[5]} you are invited')
print(f'{people_list[6]} you are invited')
print("I can invite only two people for dinner")
print(people_list)
rg_1=people_list.pop()
print(f'Sorry {rg_1} , I am cancelling your invitation')
rg_2=people_list.pop()
print(f'Sorry {rg_2} , I am cancelling your invitation')
rg_3=people_list.pop()
print(f'Sorry {rg_3} , I am cancelling your invitation')
rg_4=people_list.pop()
print(f'Sorry {rg_4} , I am cancelling your invitation')
rg_5=people_list.pop()
print(f'Sorry {rg_5} , I am cancelling your invitation')

print(people_list)

print(f'{people_list[0]} You are still invited')
print(f'{people_list[1]} You are still invited')
print("Number of people invited: ",len(people_list))

del people_list[0]
del people_list[0]

print(people_list)