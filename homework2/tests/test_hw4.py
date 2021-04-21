from tasks import hw4

cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

print(val_1)
print(val_2)
print(val_1 is val_2)


def check_if_value_is_cached():
    """Testing if value is cached"""
    assert val_1 is val_2
