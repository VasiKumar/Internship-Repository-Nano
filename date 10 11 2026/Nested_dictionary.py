student={
    "name":"Rahul",
    "age": 25,
    "Subject":{
        "phy":60,
        "chem":70,
        "math":60
    }
}

print("Math Marks: ",student["Subject"]["math"])
student["city"]="BBSR"
print(student.keys())

student.update({"branch":"CSE"})
print(student.keys())

student.update({"branch":"EEE", "roll":55})
print(student.keys())

