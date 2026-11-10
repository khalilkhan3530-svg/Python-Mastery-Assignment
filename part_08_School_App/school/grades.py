
# Calculate student average
def calculate_average(marks):
    return sum(marks) / len(marks)


# Assign grade based on average
def calculate_grade(avg):
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
