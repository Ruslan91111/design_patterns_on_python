from abc import ABC


# Класс представляющий одновременно примитивы и контейнеры
class Graphic(ABC):
    def draw(self):
        raise NotImplementedError()

    def add(self, obj):
        raise NotImplementedError()

    def remove(self, obj):
        raise NotImplementedError()

    def get_child(self, index):
        raise NotImplementedError()


class Line(Graphic):
    def draw(self):
        print('Линия')


class Rectangle(Graphic):
    def draw(self):
        print('Прямоугольник')


class Text(Graphic):
    def draw(self):
        print('Текст')


class Picture(Graphic):
    def __init__(self):
        self._children = []

    def draw(self):
        print('Изображение')

        # Вызываем отрисовку у всех дочерних объектов в списке self._children.
        for obj in self._children:
            obj.draw()

    def add(self, obj):
        # Добавить в список.
        if isinstance(obj, Graphic) and not obj in self._children:
            self._children.append(obj)

    def remove(self, obj):
        # Удалить из списка.
        index = self._children.index(obj)
        del self._children[index]

    def get_child(self, index):
        return self._children[index]


picture = Picture()
picture.add(Line())
picture.add(Rectangle())
picture.add(Text())

picture.draw()  # Все содержимое


line = picture.get_child(0)
line.draw()

