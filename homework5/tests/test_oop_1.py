from homework5.tasks.oop_1 import Student, Teacher
import datetime


def test_teacher():
    teacher = Teacher("Shadrin", "Daniil")
    assert teacher.last_name == "Shadrin"
    assert teacher.first_name == "Daniil"


def test_student():
    student = Student("Petrov", "Roman")
    assert student.last_name == "Petrov"
    assert student.first_name == "Roman"


def test_expired():
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    expired_homework = teacher.create_homework("Learn functions", 0)
    print(
        f"Just like in 'Example: 2019-05-26 16:44:30.688762': {expired_homework.created}"
    )
    assert expired_homework.deadline == datetime.timedelta(days=0)
    assert expired_homework.text == "Learn functions"
    assert student.do_homework(expired_homework) == None


def test_homework():
    teacher = Teacher("Shadrin", "Daniil")
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    assert oop_homework.deadline == datetime.timedelta(days=5)

    oop_homework2 = create_homework_too("create 2 simple classes", 2)
    assert oop_homework2.deadline == datetime.timedelta(days=2)
