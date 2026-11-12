#WAP to enter the marks of 3 subjects from user & store them in dictionary: 

dict={}
for i in range(0,3):
    subject = input("Enter the subject: ")
    mark= int(input("Enter the mark : "))
    dict[subject]= mark

print(dict)