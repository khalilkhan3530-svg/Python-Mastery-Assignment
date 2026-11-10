
# Check student attendance
def attendance_message(name, present_days, total_days):
    percentage = (present_days / total_days) * 100

    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    return f"{name}: Attendance = {percentage:.1f}%, Status = {status}"
