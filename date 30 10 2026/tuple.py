"""
1. Tuple are used to store items to a single variiable
2. It is immutable / unchangable
"""

tuple1=(1,5,8,10, "Rahul", 5.2)

print(tuple1)

print(type(tuple1))

tuple2=("rahul", "dibya", "Vivek")

tuple3 = tuple(["rahul", "dibya", "Vivek"])
print(tuple3)

tup=(1)
tup2=("rahul",)
print(type(tup))
print(type(tup2))

tuple4=tuple2+tuple3
print(tuple4)

