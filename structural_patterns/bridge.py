from abc import ABC, abstractmethod


class TVBaseClass(ABC):
    """Абстрактный телевизор"""
    @abstractmethod
    def tune_channel(self, channel):
        raise NotImplementedError()


class SonyTV(TVBaseClass):
    """Телевизор Sony"""
    def tune_channel(self, channel):
        print('Sony TV: выбран %d канал' % channel)


class LgTV(TVBaseClass):
    """Телевизор LG"""
    def tune_channel(self, channel):
        print('Lg TV: выбран %d канал' % channel)


class RemoteControlBase(ABC):
    """Абстрактный пульт управления"""
    def __init__(self):
        self._tv = self.get_tv()

    @abstractmethod
    def get_tv(self):
        raise NotImplementedError()

    def tune_channel(self, channel):
        self._tv.tune_channel(channel)


class RemoteControl(RemoteControlBase):
    """Пульт управления"""
    def __init__(self):
        super().__init__()
        self._channel = 0  # текущий канал

    def get_tv(self):
        return LgTV()

    def tune_channel(self, channel):
        super().tune_channel(channel)
        self._channel = channel

    def next_channel(self):
        self._channel += 1
        self.tune_channel(self._channel)

    def previous_channel(self):
        self._channel -= 1
        self.tune_channel(self._channel)


remote_control = RemoteControl()
remote_control.tune_channel(5)
remote_control.next_channel()

