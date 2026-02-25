students = {
    "Ivan": {"Math": 5, "Python": 6},
    "Maria": {"Math": 6, "Python": 6}
}

def add_grade(student, subject, grade):
    if student not in students:
        students[student] = {}
    
    students[student][subject] = grade
    print(f"Added {grade} in {subject} for {student}.")

def get_average(student):
    if student in students:
        grades = students[student].values()
        avg = sum(grades) / len(grades)
        return f"{student}'s Average: {avg:.2f}"
    return "Student not found!"

add_grade("Ivan", "English", 4)
add_grade("George", "Python", 6)
add_grade("George", "Math", 5)

print("\n--- Student Records ---")
for name in students:
    print(f"{name}: {students[name]}")

print("\n--- Statistics ---")
print(get_average("George"))
print(get_average("Ivan"))
