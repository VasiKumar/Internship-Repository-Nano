subjects={
    "Maths":None,
    "English":None,
    "Hindi":None
}

for key,value in subjects.items():
    subjects[key]=int(input(f"Enter marks {key} :"))

print(subjects)