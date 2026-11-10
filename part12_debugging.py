# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

print("========== Fix 3 Bugs ==========")

marks = [90, 25, 70]
passing = []

# Check every mark in the list
for m in marks:
    if m > 33:
        passing.append(m)

# Calculate the average of passing marks
average = sum(passing) / len(passing)

print("Passing Marks:", passing)
print("Average of Passing Marks:", average)

print("================================")
