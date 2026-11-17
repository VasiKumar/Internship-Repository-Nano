#In this case the numbers must be unique otherwise code won't work.

n=int(input("Enter number 1: "))
m=int(input("Enter number 2: "))
p=int(input("Enter number 3: "))

if(n>m and n>p):
    print(f"{n} is greatest i.e. first number.")
elif(m>p):
    print(f"{m} is greatest i.e. second number.")
else:
    print(f"{p} is greatest i.e. third number.")