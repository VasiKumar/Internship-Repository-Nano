temp=(1,4,8,9,10,50,20)
n=100
flag=0
i=0
while(i!=len(temp)-1):
    if(temp[i]==n):
        print("Found at ",i+1)
        flag=1
        break
    else:
        i=i+1
if(flag==0): 
    print("Not found")