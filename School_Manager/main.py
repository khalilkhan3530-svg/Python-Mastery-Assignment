
# Name: Muhammad Khalil
# Roll Number: Your Roll Number
# Date: 10-11-2026

import logging

from school.manager import SchoolManager


# Display the main menu
def show_menu() -> None:
    print("\n========== School Manager ==========")
    print("1. Add Student")
    print("2. Add Marks")
    print("3. Show Report Card")
    print("4. Class Ranking")
    print("5. Save and Exit")
    print("====================================")


# Run the school management application
def main() -> None:
    manager = SchoolManager()
    manager.load_data()

    while True:
        show_menu()

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter student name: ").strip()
                roll_number = int(input("Enter roll number: "))

                if not name:
                    raise ValueError("Name cannot be empty")

                manager.add_student(name, roll_number)
                print("Student added successfully!")

            elif choice == "2":
                roll_number = int(input("Enter roll number: "))
                marks = int(input("Enter marks: "))

                manager.add_marks(roll_number, marks)
                print("Marks added successfully!")

            elif choice == "3":
                roll_number = int(input("Enter roll number: "))
                student = manager.find_student(roll_number)

                print("\n========== Report Card ==========")
                print("Name:", student.name)
                print("Roll Number:", student.roll_number)
                print("Marks:", student.marks)
                print(f"Average: {student.average():.1f}")
                print("Grade:", student.grade())
                print("=================================")

            elif choice == "4":
                ranking = manager.class_ranking()

                print("\n========== Class Ranking ==========")

                for position, student in enumerate(ranking, start=1):
                    print(
                        f"{position}. {student.name} - "
                        f"Average: {student.average():.1f}"
                    )

                print("===================================")

            elif choice == "5":
                manager.save_data()
                print("Data saved. Exiting School Manager.")
                break

            else:
                print("Invalid choice! Please select 1 to 5.")

        except ValueError as error:
            print("Error:", error)

        except Exception:
            logging.exception("Unexpected error occurred")
            print("Something went wrong. Please try again.")


if __name__ == "__main__":
    main()
