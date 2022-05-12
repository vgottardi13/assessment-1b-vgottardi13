
group_1 = input('Enter 6 numbers separated by space: ')
group_2 = input('Enter 5 numbers separated by spaces: ')

list1 = list(group_1.split( ))
list2 = list(group_2.split( ))
print()
print(list1)
print(list2)
print()
print("Duplicated Numbers:")
for i in list1:
    if i in(list2):
        print(i, end=" ")




