students = {
    "Rahul":85,
    "Anita":92,
    "Suresh":80,
    "Priya":70,
}

name=input("Enter student name")

if name in students:
    print(f"{name}'s marks are: {students[name]}")
else:
    print("Student not found")