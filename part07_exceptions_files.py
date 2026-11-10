# Name: Muhammad Khalil
# Roll Number: TRN-2026-000376
# Date: 10-11-2026

print("==========Safe Division==========")

# Keep asking until valid numbers are entered
while True:
    try:
        # Get two numbers from the user
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Divide the numbers
        result = num1 / num2

    except ValueError:
        print("Invalid input! Please enter numbers only.")

    except ZeroDivisionError:
        print("Cannot divide by zero! Try again.")

    else:
        print(f"Result: {result}")
        break

print("==========End of Task 1==========")


print("==========Daily Diary==========")

from datetime import date

# Display menu
while True:
    print("\n1. Add a new entry")
    print("2. View all entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Get today's note
        note = input("Write your daily note: ")

        # Append the note to the diary file
        with open("diary.txt", "a") as file:
            file.write(f"{date.today()} - {note}\n")

        print("Entry saved successfully!")

    elif choice == "2":
        # Read all saved entries
        try:
            with open("diary.txt", "r") as file:
                entries = file.read()

            print("\n==========Past Entries==========")
            print(entries)

        except FileNotFoundError:
            print("No entries yet")

    elif choice == "3":
        print("Exiting Diary...")
        break

    else:
        print("Invalid choice! Try again.")

print("==========End of Task 2==========")



print("==========CSV Result Sheet==========")

import csv
import json

# Student result sheet
result_sheet = {
    "Ali": [80, 72, 91],
    "Sara": [95, 88, 90],
    "Ahmed": [40, 35, 50],
    "Hassan": [30, 25, 20],
    "Usman": [70, 75, 80]
}

# Save student data to CSV file
with open("results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    # Write column headings
    writer.writerow(["Name", "Mark1", "Mark2", "Mark3", "Average"])

    for name, marks in result_sheet.items():
        avg = sum(marks) / len(marks)

        writer.writerow([name, marks[0], marks[1], marks[2], avg])

# Read CSV file and find the topper
with open("results.csv", "r") as file:
    reader = csv.DictReader(file)

    topper = ""
    highest_average = 0

    for row in reader:
        average = float(row["Average"])

        if average > highest_average:
            highest_average = average
            topper = row["Name"]

print(f"Topper: {topper}")
print(f"Average: {highest_average:.2f}")

# Save the same data to JSON file
with open("results.json", "w") as file:
    json.dump(result_sheet, file, indent=4)

print("CSV and JSON files saved successfully!")

print("==========End of Task 3==========")

