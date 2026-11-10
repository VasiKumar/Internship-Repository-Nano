print("Method 1: ")
list1 = [1, 2, 3, 2, 1]

i = 0
j = len(list1) - 1

while i < j:
    if list1[i] != list1[j]:
        print("not palindrome")
        break
    i += 1
    j -= 1
else:
    print("palindrome")

print("Method 2: ")
if(list1== list1[::-1]):
    print("palindrome")
else:
    print("Not palindrome")