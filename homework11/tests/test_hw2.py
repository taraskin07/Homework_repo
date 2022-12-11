from homework11.tasks.hw2 import Order


def morning_discount(price):
    discount_price = price * 0.5
    return discount_price


def elder_discount(price):
    discount_price = price * 0.1
    return discount_price


def another_discount(price):
    discount_order = 0.17
    return price - price * discount_order


def test_order_class_with_different_discounts():
    order_morning = Order(100, morning_discount)
    order_17 = Order(100, another_discount)
    order_3elder = Order(100, elder_discount)
    assert order_morning.final_price() == 50.0
    assert order_17.final_price() == 83.0
    assert order_3elder.final_price() == 10.0
