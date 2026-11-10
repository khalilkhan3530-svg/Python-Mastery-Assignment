
# Calculate the average marks
def average(marks):
    return sum(marks) / len(marks)


# Calculate the grade
def grade(avg):
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


# Generate student report
def report(name, marks):
    avg = average(marks)
    student_grade = grade(avg)

    return f"{name}: Average = {avg:.1f}, Grade = {student_grade}"
