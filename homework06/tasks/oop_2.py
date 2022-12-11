import datetime
import logging
from collections import defaultdict

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


class DeadlineError(Exception):
    """Класс исключений, для вывода сообщения об ошибке"""

    pass


class Homework:
    """
    Класс Homework принимает на вход 2 атрибута: текст задания и количество дней на это задание.

    :param text: текст задания
    :param deadline: количество дней на задание
    """

    def __init__(self, text, deadline):
        """
        Конструктор
        """
        self.text = text
        logger.debug(f"Task text: {self.text}")
        time_now = datetime.datetime.now()
        self.created = time_now
        self.deadline = datetime.timedelta(days=deadline)

    def is_active(self):
        """
        Проверяет, не прошел ли дедлайн.

        :param isactive: разница между текущим временем и временем получения задания

        :return: True -время ещё есть, False -дедлайн прошел
        :rtype: bool
        """
        isactive = datetime.datetime.now() - self.created
        return isactive < self.deadline


class HomeworkResult:

    """Принимает объект автора задания, принимает исходное задание
    и его решение в виде строки.

        :param homework: для объекта :class:`Homework'. Если передан не этот класс -  выкинуть
        подходящие по смыслу исключение с сообщением:
        'You gave a not Homework object'

        :param solution: хранит решение ДЗ как строку
        :param student: хранит объект :class:`Student'
        :param created: точная дата и время создания

        :raises [TypeError]: [сообщение об ошибке: 'You gave a not Homework object']
    """

    def __init__(self, homework=None, solution=None, student=None):
        """Конструктор"""
        if isinstance(homework, Homework):
            self.homework = homework
        else:
            raise TypeError("You gave a not Homework object")
        self.solution = solution
        self.student = student
        self.created = datetime.datetime.now()


class Person:
    """Избавляемся от дублирования с помощью наследования
    для :class:'Student' и :class:'Teacher'"""

    def __init__(self, last_name, first_name):
        """Конструктор"""
        self.last_name = last_name
        self.first_name = first_name


class Student(Person):
    """
    Наследован от Person. Принимает на вход имя и фамилию студента.

    :param last_name: фамилия студента
    :param first_name: имя студента
    """

    def __init__(self, last_name, first_name):
        """Конструктор"""
        super().__init__(last_name, first_name)

    def do_homework(self, homework=None, solution=None, student=None):
        """
        Принимает объект homework и возвращает его же, если задание уже просрочено, то печатет 'You are late' и возвращает None.

        :param homework: Принимает объект homework :class:`Homework`
        :param solution: хранит решение ДЗ как строку
        :param student: хранит объект :class:`Student'

        :raises [DeadlineError]: [с сообщением 'You are late' вместо print]

        :return: возвращает :class:'HomeworkResult'
        :rtype: :class:'HomeworkResult'
        """
        if homework.is_active():
            return HomeworkResult(homework, solution, student)
        else:
            raise DeadlineError("You are late")


class Teacher(Person):
    """
    Наследован от Person. Принимает на вход имя и фамилию учителя.

    :param last_name: фамилия учителя
    :param first_name: имя учителя
    """

    homework_done = defaultdict(set)

    def __init__(self, last_name, first_name):
        """Конструктор"""
        super().__init__(last_name, first_name)

    @staticmethod
    def create_homework(text, days_amount):
        """Принимает текст задания и количество дней на это задание,
        возвращает экземпляр Homework

            :param text: текст задания
            :param days_amount: количество дней на это задание

            :return: экземпляр класса :class:`Homework`
            :rtype: :class:`Homework`
        """
        return Homework(text, days_amount)

    def check_homework(self, homeworkresult):
        """Принимает экземпляр :class:'HomeworkResult' и возвращает True если
        ответ студента больше 5 символов, так же при успешной проверке добавить в
        homework_done. Если меньше 5 символов - никуда не добавлять и вернуть False.
            :param homeworkresult: :class:'HomeworkResult' object.
            :return: `True` при успешной проверке, `False` если меньше 5 символов
            :rtype: bool
        """
        homework = homeworkresult.homework
        symb_len = homeworkresult.solution
        if len(symb_len) > 5:
            self.homework_done[homework].add(homeworkresult.solution)
            return True
        return False

    @classmethod
    def reset_results(cls, homework=None):
        """Если передать экземпляр Homework - удаляет только
        результаты этого задания из homework_done, если ничего не передавать,
        то полностью обнулит homework_done.
            :param homework: экземпляр :class:'HomeworkResult'
        """
        if homework is None:
            cls.homework_done = defaultdict(list)
        else:
            cls.homework_done[homework] = []


if __name__ == "__main__":
    opp_teacher = Teacher("Shadrin", "Daniil")
    advanced_python_teacher = Teacher("Smetanin", "Aleksandr")

    lazy_student = Student("Petrov", "Roman")
    good_student = Student("Sokolov", "Lev")

    oop_hw = opp_teacher.create_homework("Learn OOP", 1)
    docs_hw = opp_teacher.create_homework("Read docs", 5)

    result_1 = good_student.do_homework(oop_hw, "I have done this hw")
    result_2 = good_student.do_homework(docs_hw, "I have done this hw too")
    result_3 = lazy_student.do_homework(docs_hw, "done")
    try:
        result_4 = HomeworkResult(good_student, "fff", "Solution")
    except Exception:
        print("There was an exception here")
    opp_teacher.check_homework(result_1)
    temp_1 = opp_teacher.homework_done

    advanced_python_teacher.check_homework(result_1)
    temp_2 = Teacher.homework_done
    assert temp_1 == temp_2

    print(opp_teacher.check_homework(result_2))
    print(opp_teacher.check_homework(result_3))

    print(Teacher.homework_done[oop_hw])
    Teacher.reset_results()
