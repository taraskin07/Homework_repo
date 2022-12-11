"""
You are given the following code:

class Order:
    morning_discount = 0.25

    def __init__(self, price):
        self.price = price

    def final_price(self):
        return self.price - self.price * self.morning_discount

Make it possible to use different discount programs.
Hint: use strategy behavioural OOP pattern.
https://refactoring.guru/design-patterns/strategy

Example of the result call:

def morning_discount(order):
    ...

def elder_discount(order):
    ...

order_1 = Order(100, morning_discount)
assert order_1.final_price() == 50

order_2 = Order(100, elder_discount)
assert order_1.final_price() == 10
"""


class Order:
    def __init__(self, price, discount):

        self.price = price
        self.discount = discount

    def final_price(self):
        return self.discount(self.price)


if __name__ == "__main__":

    def morning_discount(price):
        discount_price = price * 0.5
        return discount_price

    def elder_discount(price):
        discount_price = price * 0.1
        return discount_price

    order_1 = Order(100, morning_discount)
    print(order_1.final_price())

    order_2 = Order(100, elder_discount)
    print(order_2.final_price())
