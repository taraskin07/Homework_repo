"""
Необходимо создать 3 класса и взаимосвязь между ними (Student, Teacher,
Homework)
Наследование в этой задаче использовать не нужно.
Для работы с временем использовать модуль datetime

1. Homework принимает на вход 2 атрибута: текст задания и количество дней
на это задание
Атрибуты:
    text - текст задания
    deadline - хранит объект datetime.timedelta с количеством
    дней на выполнение
    created - c точной датой и временем создания
Методы:
    is_active - проверяет не истекло ли время на выполнение задания,
    возвращает boolean

2. Student
Атрибуты:
    last_name
    first_name
Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None

3. Teacher
Атрибуты:
     last_name
     first_name
Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.

PEP8 соблюдать строго.
Всем перечисленным выше атрибутам и методам классов сохранить названия.
К названием остальных переменных, классов и тд. подходить ответственно -
давать логичные подходящие имена.
"""
import datetime


class Homework:
    """
    Класс Homework принимает на вход 2 атрибута: текст задания и количество дней на это задание.
    """

    def __init__(self, text, deadline):
        """
        Текст задания и количество дней на это задание
        """
        self.text = text
        # print(self.text)
        time_now = datetime.datetime.now()
        self.created = time_now
        self.deadline = datetime.timedelta(days=deadline)

    def is_active(self):
        isactive = datetime.datetime.now() - self.created
        return isactive < self.deadline


class Student:
    """
    Атрибуты:
    last_name
    first_name
    Методы:
    do_homework - принимает объект Homework и возвращает его же,
    если задание уже просрочено, то печатет 'You are late' и возвращает None.
    """

    def __init__(self, last_name, first_name):
        """Текст задания и количество дней на это задание"""
        self.last_name = last_name
        # print(self.last_name)
        self.first_name = first_name
        # print(self.first_name)

    def do_homework(self, Homework):
        """
        Принимает объект Homework и возвращает его же, если задание уже просрочено, то печатет 'You are late' и возвращает None.
        """
        self.Homework = Homework
        if Homework.is_active():
            return Homework
        else:
            print("You are late")


class Teacher:
    """
    Атрибуты:
    last_name
     first_name
    Методы:
    create_homework - текст задания и количество дней на это задание,
    возвращает экземпляр Homework
    Обратите внимание, что для работы этого метода не требуется сам объект.
    """

    def __init__(self, last_name, first_name):
        self.last_name = last_name
        # print(self.last_name)
        self.first_name = first_name
        # print(self.first_name)

    def create_homework(self, text, days_amount):
        self.text = text
        self.days_amount = days_amount
        return Homework(self.text, self.days_amount)


if __name__ == "__main__":
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    print(teacher.first_name)  # Daniil
    print(student.last_name + "\n")  # Petrov

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(
        f"Just like in 'Example': {expired_homework.created}"
    )  # Example: 2019-05-26 16:44:30.688762
    print(expired_homework.deadline)  # 0:00:00
    print(expired_homework.text + "\n")  # 'Learn functions'

    # create function from method and use it
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(str(oop_homework.deadline) + "\n")  # 5 days, 0:00:00

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)  # You are late
