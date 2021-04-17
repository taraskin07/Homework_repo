def check_power_of_2(a: int) -> bool:
    a = int(a)
    return not (a & (a - 1))


if __name__ == "__main__":
    a = input("Enter a number: ")
    print(check_power_of_2(a))
