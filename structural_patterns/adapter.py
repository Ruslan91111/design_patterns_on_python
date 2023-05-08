import math


class AbstractHole:
    """ Абстрактная дырка. """
    def __init__(self, radius):
        # задаем радиус дыры
        self.radius = radius

    def put(self, obj):
        # пытаемся просунуть объект через дырку
        try:
            # Чтобы объект пролез, нужно, чтобы радиус дырки позволял.
            if self.radius >= obj.adjust:
                print('Проходит!')
            else:
                print('Не проходит')

        except AttributeError:
            print('Переданный адаптер не проходит! Напишите Адаптер на python!')


class Square:
    """ Абстрактный класс, который будем пытаться пропустить через дырку. """
    def __init__(self, width, height):
        # Зададим параметры ширины и высоты.
        self.width = width
        self.height = height


class SquareHoleAdapter:
    """ Адаптер для затычки."""
    def __init__(self, square_object):
        self.square_object = square_object

    @property
    def adjust(self):
        # половина диагонали квадрата будет как раз влезать
        # в дырку радиусом с полученное значение
        return math.sqrt(2 * (self.square_object.width ** 2)) / 2


first_hole = AbstractHole(5)
second_hole = AbstractHole(2)

square_1 = Square(2, 3)
square_2 = Square(3, 3)

square_adapter = SquareHoleAdapter(square_2)

first_hole.put(square_1)
first_hole.put(square_adapter)
second_hole.put(square_adapter)
