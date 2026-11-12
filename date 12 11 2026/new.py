#WAP to enter the marks of 3 subjects from user & store them in dictionary: 
subjects={
    
}
x=[]

for i in range(0,3):
    x.append ( input(f"Enter key :"))
for j in x:
    subjects[j]= int(input("Enter the marks: "))
    

print(subjects)