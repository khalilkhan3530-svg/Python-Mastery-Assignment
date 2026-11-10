
from dataclasses import dataclass, field


# Create a Student class
@dataclass
class Student:
    name: str
    roll_number: int
    marks: list[int] = field(default_factory=list)

    # Add marks to the student
    def add_marks(self, mark: int) -> None:
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

        self.marks.append(mark)

    # Calculate average marks
    def average(self) -> float:
        if not self.marks:
            return 0.0

        return sum(self.marks) / len(self.marks)

    # Calculate student grade
    def grade(self) -> str:
        avg = self.average()

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
