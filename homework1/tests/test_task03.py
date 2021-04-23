from homework1.tasks.task03 import find_maximum_and_minimum

with open("task03.txt", "r") as fi:

    def test_min_and_max_in_file():
        """Testing that function return minimum -15 and maximum 566 from *.txt file"""
        assert find_maximum_and_minimum(fi) == (-15, 566)


fi.close()
