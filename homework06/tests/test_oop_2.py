import pytest

from homework06.tasks.oop_2 import HomeworkResult, Student, Teacher


def test_dictionary_teacher():
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")

    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")

    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done
    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    assert opp_teacher.check_homework(result_2)
    assert not opp_teacher.check_homework(result_3)

    Teacher.reset_results()
    assert len(Teacher.homework_done) == 0


def test_exceptions():
    good_student = Student("Sokolov", "Lev")
    with pytest.raises(TypeError):
        HomeworkResult(good_student, "fff", "Solution")
