students = {"Ben": 1, "Jan": 2, "Peter": 1, "Melissa": 4}
print(students)

# lesen
student_1 = students["Ben"]
print(student_1)

# schreiben
students["Ben"] = 6
print(students)

# hinzufügen
students["Julia"] = 2
print(students)

# löschen
students.pop("Julia")
print(students)

# Keys
for student_name in students:
    print(student_name)

# Values
for student_grade in students.values():
    print(student_grade)

# Keys and Values
for key, value in students.items():
    print(key, value)
