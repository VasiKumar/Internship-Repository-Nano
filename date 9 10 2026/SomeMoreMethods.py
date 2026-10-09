list=[5,6,3,1,4]
list1 = [3,7,9,5]

list.clear()
print(list)
list=[13,43,4,42,423,4]
list2= list.copy()
print(list2)

abc=[1,2,2,2,2,26,7,7,7,1,1,1,2]
print("Number of occurence of 2 :",abc.count(2))

list.extend(abc)
print(list)

print(list.index(2))

del list[0]
print(list)
del list1
print(list1)
print(type(list1))
# list.append(3)
# print(list)