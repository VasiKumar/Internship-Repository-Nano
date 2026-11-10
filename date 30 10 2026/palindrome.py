list1=[1,2,3,2,1]
list2=list1.copy()

list2.reverse()
if(list1 == list2):
    print("Is is a palindrome")

else:
    print("Not palindrome")