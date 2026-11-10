
import pytest

from school.manager import SchoolManager


# Create a fresh school manager for each test
@pytest.fixture
def manager():
    return SchoolManager()


# Test adding a student
def test_add_student(manager):
    manager.add_student("Ali", 101)

    assert len(manager.students) == 1
    assert manager.students[0].name == "Ali"


# Test duplicate roll number
def test_duplicate_roll_number(manager):
    manager.add_student("Ali", 101)

    with pytest.raises(ValueError):
        manager.add_student("Ahmed", 101)


# Test adding marks
def test_add_marks(manager):
    manager.add_student("Ali", 101)
    manager.add_marks(101, 90)

    assert manager.students[0].marks == [90]


# Test invalid marks
def test_invalid_marks(manager):
    manager.add_student("Ali", 101)

    with pytest.raises(ValueError):
        manager.add_marks(101, 110)


# Test finding a student
def test_find_student(manager):
    manager.add_student("Sara", 102)

    student = manager.find_student(102)

    assert student.name == "Sara"


# Test class ranking
def test_class_ranking(manager):
    manager.add_student("Ali", 101)
    manager.add_student("Sara", 102)

    manager.add_marks(101, 70)
    manager.add_marks(102, 90)

    ranking = manager.class_ranking()

    assert ranking[0].name == "Sara"
    assert ranking[1].name == "Ali"


# Test saving and loading student data
def test_save_and_load(manager, tmp_path):
    manager.add_student("Ali", 101)
    manager.add_marks(101, 85)

    file_path = tmp_path / "school.json"
    manager.save_data(str(file_path))

    new_manager = SchoolManager()
    new_manager.load_data(str(file_path))

    assert new_manager.students[0].name == "Ali"
    assert new_manager.students[0].marks == [85]
