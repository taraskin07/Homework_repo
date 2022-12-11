from homework6.tasks.counter import instances_counter


@instances_counter
class User:
    pass


def test_count_instances():
    user, _, _ = User(), User(), User()
    assert user.get_created_instances() == 3


def test_count_instances_no_reset():
    assert User.reset_instances_counter() == 3


def test_child_class():
    @instances_counter
    class User:
        instances = 0

        def __init__(self, arg):
            self.instances = arg

    class Admin(User):
        pass

    Admin.reset_instances_counter()
    Admin(User), Admin(User), Admin(User)
    assert Admin.get_created_instances() == 3

    class Devops(Admin):
        pass

    Devops(Admin), Devops(Admin), Devops(Admin)
    assert Devops.get_created_instances() == 3
