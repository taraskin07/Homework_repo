"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    """Some code"""

    class Gnrl_counter(cls):
        instances = 0

        @classmethod
        def init_counter(cls):
            if not "instances" in cls.__dict__:
                cls.instances = 0

        def __init__(self, *args, **kwargs):
            self.init_counter()
            super().__init__(*args, **kwargs)
            self.__class__.instances += 1

        @classmethod
        def get_created_instances(cls):
            cls.init_counter()
            return cls.instances

        @classmethod
        def reset_instances_counter(cls):
            cls.init_counter()
            return cls.instances

    return Gnrl_counter


@instances_counter
class User:
    pass


if __name__ == "__main__":

    print(User.get_created_instances())  # 0
    user, _, _ = User(), User(), User()
    print(user.get_created_instances())  # 3
    print(user.reset_instances_counter())  # 3
