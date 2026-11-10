
import json
import logging
from pathlib import Path

from school.models import Student


# Configure logging
logging.basicConfig(
    filename="school.log",
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)


# Store and manage students
class SchoolManager:

    def __init__(self):
        self.students: list[Student] = []

    # Add a new student
    def add_student(self, name: str, roll_number: int) -> None:
        for student in self.students:
            if student.roll_number == roll_number:
                raise ValueError("Roll number already exists")

        student = Student(name, roll_number)
        self.students.append(student)
        logging.info("Student added: %s", name)

    # Find a student using roll number
    def find_student(self, roll_number: int) -> Student:
        for student in self.students:
            if student.roll_number == roll_number:
                return student

        raise ValueError("Student not found")

    # Add marks to a student
    def add_marks(self, roll_number: int, mark: int) -> None:
        student = self.find_student(roll_number)
        student.add_marks(mark)
        logging.info("Marks added for roll number: %s", roll_number)

    # Get students sorted by average marks
    def class_ranking(self) -> list[Student]:
        return sorted(
            self.students,
            key=lambda student: student.average(),
            reverse=True
        )

    # Save student data to JSON
    def save_data(self, filename: str = "school.json") -> None:
        data = [
            {
                "name": student.name,
                "roll_number": student.roll_number,
                "marks": student.marks
            }
            for student in self.students
        ]

        Path(filename).write_text(json.dumps(data, indent=4))
        logging.info("School data saved")

    # Load student data from JSON
    def load_data(self, filename: str = "school.json") -> None:
        path = Path(filename)

        if not path.exists():
            return

        data = json.loads(path.read_text())

        self.students = [
            Student(**student_data)
            for student_data in data
        ]

        logging.info("School data loaded")
