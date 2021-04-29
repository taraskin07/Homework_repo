from typing import List


def fizzbuzz(n: int) -> List[str]:
    """Return the list of str up to n as FizzBuzz numbers

    >>> fizzbuzz(5)
    ['1', '2', 'fizz', '4', 'buzz']
    >>> fizzbuzz(23)
    ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizz buzz', '16', '17', 'fizz', '19', 'buzz', 'fizz', '22', '23']
    >>> fizzbuzz(-2)
    []

    You shouldn't use letters instead of numbers here*:
    >>> fizzbuzz('f')
    Traceback (most recent call last):
    ...
    ValueError: invalid literal for int() with base 10: 'f'
    """
    fizzbuzz_list = []
    for number in range(1, int(n) + 1):
        if (number % 3 == 0) and (number % 5 == 0):
            number = "fizz buzz"
            fizzbuzz_list.append(number)
        elif number % 5 == 0:
            number = "buzz"
            fizzbuzz_list.append(number)
        elif number % 3 == 0:
            number = "fizz"
            fizzbuzz_list.append(number)
        else:
            fizzbuzz_list.append(str(number))
    return fizzbuzz_list


if __name__ == "__main__":
    import doctest

    doctest.testmod()
