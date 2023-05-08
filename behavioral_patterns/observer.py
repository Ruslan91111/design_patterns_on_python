from abc import ABC, abstractmethod


class SubjectOfObservation(ABC):
    """Субъект"""
    def __init__(self):
        self._data = None
        self._observers = set()

    def attach(self, observer):
        # подписаться на оповещение
        if not isinstance(observer, ObserverBase):
            raise TypeError()
        self._observers.add(observer)

    def detach(self, observer):
        # отписаться от оповещения
        self._observers.remove(observer)

    def get_data(self):
        return self._data

    def set_data(self, data):
        self._data = data
        self.notify(data)

    def notify(self, data):
        # уведомить всех наблюдателей о событии
        for observer in self._observers:
            observer.update(data)


class ObserverBase(ABC):
    """Абстрактный наблюдатель"""
    @abstractmethod
    def update(self, data):
        raise NotImplementedError()


class Observer(ObserverBase):
    """Наблюдатель"""
    def __init__(self, name):
        self._name = name

    def update(self, data):
        print('%s: %s' % (self._name, data))


subject_of_observation = SubjectOfObservation()
subject_of_observation.attach(Observer('Наблюдатель 1'))
subject_of_observation.attach(Observer('Наблюдатель 2'))
subject_of_observation.set_data('данные для наблюдателя')
# Наблюдатель 2: данные для наблюдателя