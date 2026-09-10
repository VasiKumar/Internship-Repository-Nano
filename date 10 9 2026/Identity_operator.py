x=[10,20]
y=[10,20]
z=x
z=y
print(x is z)
print(y is z)
print(x is y) #checks memory location 
print(x == y)


#Works only in list
#it checks memory location 
"""

False
True
False
True

"""