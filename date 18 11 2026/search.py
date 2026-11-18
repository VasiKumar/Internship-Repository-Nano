temp=(1,4,8,9,10,50,20)
n=10
flag=0
index=0
for i in temp:
    index=index+1
    if(n==i):
        print("Found at ",index," : " ,i)
        flag=1

if(flag==0):
    print("Not found")