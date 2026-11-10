import pytest
from part_05_function import grade


# Test all grading boundaries
@pytest.mark.parametrize("marks, expected", [
    (32, "Fail"),
    (33, "D"),
    (59, "D"),
    (60, "C"),
    (69, "C"),
    (70, "B"),
    (79, "B"),
    (80, "A")
])
def test_grade(marks, expected):
    assert grade(marks) == expected


# Test marks above 100
def test_marks_above_100():
    with pytest.raises(ValueError):
        grade(101)


# Test negative marks
def test_negative_marks():
    with pytest.raises(ValueError):
        grade(-1)
