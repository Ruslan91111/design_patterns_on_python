"""Пример реализации паттерна строитель на языке python."""
from abc import ABC, abstractmethod


class Builder(ABC):
    """Абстрактный класс строитель дома"""
    @abstractmethod
    def build_floor(self):
        pass

    @abstractmethod
    def build_walls(self):
        pass

    @abstractmethod
    def build_ceil(self):
        pass

    def create_the_house(self):
        raise NotImplementedError()  # Альтернатива декоратору @abstractmethod


class WoodenBuilder(Builder):
    """Класс - конкретный строитель деревянного дома. Методы, отвечающие за сборку элементов, последний
    метод собрать дом целиком"""
    def build_floor(self):
        return Floor()

    def build_walls(self):
        return Walls()

    def build_ceil(self):
        return Ceil()

    def create_the_house(self):
        """Собрать дом целиком и вернуть объект класса House"""
        floor = self.build_floor()
        walls = self.build_walls()
        ceil = self.build_ceil()
        return House(floor, walls, ceil)


class House:
    """Дом"""
    def __init__(self, floor, walls, ceil):
        self._floor = floor
        self._walls = walls
        self._ceil = ceil

    def __str__(self):
        return 'Дом построен'


# Составляющие дома
class Floor(object):
    """Пол"""


class Walls(object):
    """Стены"""


class Ceil(object):
    """Потолок"""


class Foreman:
    def build_the_house(self, builder):
        new_house = builder.create_the_house()
        print(new_house)


wooden_builder = WoodenBuilder()
my_foreman = Foreman()
first_house = my_foreman.build_the_house(wooden_builder)


# Строитель (Builder) — паттерн, порождающий объекты.
# Отделяет конструирование сложного объекта от его представления, так что в результате одного и того же
# процесса конструирования могут получаться разные представления.
# От абстрактной фабрики отличается тем, что делает акцент на пошаговом конструировании объекта.
# Строитель возвращает объект на последнем шаге, тогда как абстрактная фабрика возвращает объект немедленно.
# Строитель часто используется для создания паттерна компоновщик.
