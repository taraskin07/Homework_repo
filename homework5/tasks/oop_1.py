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
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

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
        logger.debug(f'Task text: {self.text}')
        time_now = datetime.datetime.now()
        self.created = time_now
        self.deadline = datetime.timedelta(days=deadline)

    def is_active(self):
        """
        Проверяет, не прошел ли дедлайн.

        :param isactive: разница между текущим временем и временем получения задания

        :return: True -время ещё есть, False -дедлайн прошел
        :type: bool
        """
        isactive = datetime.datetime.now() - self.created
        return isactive < self.deadline


class Student:
    """
    Принимает на вход имя и фамилию студента.

    :param last_name: фамилия студента
    :param first_name: имя студента
    """

    def __init__(self, last_name, first_name):
        """Конструктор"""
        self.last_name = last_name
        logger.debug(f'Last name: {self.last_name}')
        self.first_name = first_name
        logger.debug(f'First name: {self.first_name}')

    def do_homework(self, homework):
        """
        Принимает объект homework и возвращает его же, если задание уже просрочено, то печатет 'You are late' и возвращает None.

        :param homework: Принимает объект homework :class:`Homework`

        :return: возвращает объект :class:`Homework`, есди задание просрочено, то :class:`NoneType`
        :type: объект :class:`Homework`  или объект :class:`NoneType`
        """
        self.homework = homework
        if homework.is_active():
            return homework
        else:
            print("You are late")


class Teacher:
    """
    Принимает на вход имя и фамилию учителя.

    :param last_name: фамилия учителя
    :param first_name: имя учителя
    """

    def __init__(self, last_name, first_name):
        """Конструктор"""
        self.last_name = last_name
        logger.debug(print(f'Last name: {self.last_name}'))
        self.first_name = first_name
        logger.debug(print(f'First name: {self.first_name}'))

    def create_homework(self, text, days_amount):
        """Принимает текст задания и количество дней на это задание,
    возвращает экземпляр Homework

        :param text: текст задания
        :param days_amount: количество дней на это задание

        :return: экземпляр класса :class:`Homework`
        """
        self.text = text
        self.days_amount = days_amount
        return Homework(self.text, self.days_amount)


if __name__ == "__main__":
    teacher = Teacher("Shadrin", "Daniil")
    student = Student("Petrov", "Roman")
    print(teacher.first_name)
    logger.debug('# Daniil')
    print(student.last_name)
    logger.debug('# Petrov')
    print("\n")

    expired_homework = teacher.create_homework("Learn functions", 0)
    print(
        f"Just like in 'Example': {expired_homework.created}"
    )
    logger.debug(f'# Example: 2019-05-26 16:44:30.688762')
    print(expired_homework.deadline)
    logger.debug('# 0:00:00')
    print(expired_homework.text)
    logger.debug('# Learn functions')
    print("\n")

    logger.debug('# create function from method and use it')
    create_homework_too = teacher.create_homework
    oop_homework = create_homework_too("create 2 simple classes", 5)
    print(str(oop_homework.deadline))
    logger.debug('# 5 days, 0:00:00')
    print("\n")

    student.do_homework(oop_homework)
    student.do_homework(expired_homework)
    logger.debug('# You are late')
