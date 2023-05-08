# Прототип — паттерн, порождающий объекты.
# Задает виды создаваемых объектов с помощью экземпляра-прототипа
# и создает новые объекты путем копирования этого прототипа.
import copy


class Prototype:
    def __init__(self):
        self._clones = {}

    def register(self, name, clone):
        self._clones[name] = clone

    def unregister(self, name):
        del self._clones[name]

    def clone_the_prototype(self, name, attrs):
        clone = copy.deepcopy(self._clones[name])
        clone.__dict__.update(attrs)
        return clone


class Bird:
    """Птица"""


prototype = Prototype()
prototype.register('bird', Bird())

owl = prototype.clone_the_prototype('bird', {'name': 'Owl'})
print(type(owl), owl.name)

duck = prototype.clone_the_prototype('bird', {'name': 'Duck'})
print(type(duck), duck.name)



