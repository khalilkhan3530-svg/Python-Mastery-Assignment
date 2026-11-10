
print("========== School Management App ==========")

# Import functions from school package
from school.grades import calculate_average, calculate_grade
from school.attendance import attendance_message

# Student data
students = {
    "Ali": [80, 90, 85],
    "Sara": [70, 75, 80],
    "Ahmed": [50, 60, 65]
}

# Display student reports
for name, marks in students.items():
    avg = calculate_average(marks)
    student_grade = calculate_grade(avg)

    print(f"\nStudent Name: {name}")
    print(f"Average Marks: {avg:.1f}")
    print(f"Grade: {student_grade}")

# Display attendance reports
print("\n========== Attendance Reports ==========")

print(attendance_message("Ali", 25, 30))
print(attendance_message("Sara", 20, 30))
print(attendance_message("Ahmed", 18, 30))

print("=========================================")
