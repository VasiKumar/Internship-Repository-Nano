thislist=[5,4,2,1]
thislist.append(3)

print(thislist)

thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)
thislist.insert(2,10)
print(thislist)

thislist.remove(3)
print(thislist)

thislist.pop(3)
print(thislist)

print(len(thislist))

print(thislist.count(10))

print(thislist.index(5))

x=thislist.copy()

x.remove(5)
print(thislist)
print(x)

print(thislist)
y=thislist

thislist.remove(4)
print(y)

