def youngest_student(students):
    min_val = float('inf')
    youngest = ""
    for student, age in students.items():
        if age < min_val:
            min_val = age
            youngest = student
    return youngest


# students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
# print(youngest_student(students))  # Expected output: "Alice"
