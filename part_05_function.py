# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

import math

print("========== Warm-up ==========")

# Calculate the area of a circle
def area_of_circle(r: float) -> float:
    return math.pi * r ** 2


# Check whether a number is even
def is_even(n: int) -> bool:
    return n % 2 == 0


# Greet a person in English or Urdu
def greet(name: str, lang: str = "en") -> str:
    if lang == "ur":
        return f"Salaam {name}"
    return f"Hello {name}"


# Test warm-up functions three times
print(area_of_circle(5))
print(area_of_circle(7))
print(area_of_circle(10))

print(is_even(10))
print(is_even(7))
print(is_even(20))

print(greet("Ali"))
print(greet("Sara", "ur"))
print(greet("Ahmed"))


print("========== Build: Student Report ==========")

# Calculate the average marks
def average(marks: list[int]) -> float:
    if not marks:
        return 0.0
    return sum(marks) / len(marks)




# Calculate the grade and validate marks
def grade(avg: float) -> str:
    if avg < 0 or avg > 100:
        raise ValueError("Marks must be between 0 and 100")

    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    else:
        return "Fail"



# Create a student report
def report(name: str, marks: list[int]) -> str:
    avg = average(marks)
    student_grade = grade(avg)
    return f"{name}: Average = {avg:.1f}, Grade = {student_grade}"


# Test the report function with three students
print(report("Ali", [80, 90, 85]))
print(report("Sara", [70, 75, 80]))
print(report("Ahmed", [50, 60, 65]))


print("========== Challenge: Comprehensions ==========")

# Create a list of squares from 1 to 10
squares = [number ** 2 for number in range(1, 11)]
print("Squares:", squares)


# Filter names that have more than four letters
names = ["Ali", "Ahmed", "Hassan", "Sara", "Muhammad"]
long_names = [name for name in names if len(name) > 4]
print("Names longer than 4 letters:", long_names)


# Create a dictionary containing student names and their averages
result_sheet: dict[str, list[int]] = {
    "Ali": [80, 90, 85],
    "Sara": [70, 75, 80],
    "Ahmed": [50, 60, 65],
    "Hassan": [30, 25, 35]
}

student_averages = {
    name: average(marks)
    for name, marks in result_sheet.items()
}
print("Student Averages:", student_averages)


# Get students who passed with an average of 33 or more
passing_students = [
    name for name, avg in student_averages.items()
    if avg >= 33
]
print("Passing Students:", passing_students)

print("==========================================")
