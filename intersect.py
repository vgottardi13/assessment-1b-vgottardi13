
group_1 = '80 50 63 20 75'
group_2 = '66 50 20 1'

list1 = list(group_1.split( ))
list2 = list(group_2.split( ))

print(list1)
print(list2)

print()

for i in list1:
    if i in(list2):
        print(i, end=" ")


