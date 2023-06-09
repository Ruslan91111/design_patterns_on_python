from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_drink(self):
        raise NotImplementedError()

    def create_food(self):
        raise NotImplementedError()


class Drink:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class Food:
    def __init__(self, name):
        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_drink(self):
        return Drink('Coca-cola')

    def create_food(self):
        return Food('Hamburger')


class ConcreteFactory2(AbstractFactory):
    def create_drink(self):
        return Drink('Pepsi')

    def create_food(self):
        return Food('Cheeseburger')


def get_set(order):
    if order == 0:
        return ConcreteFactory1()
    elif order == 1:
        return ConcreteFactory2()


set = get_set(1)
print(set.create_drink())
print(set.create_food())

