"""Фабричный метод."""
from abc import ABC, abstractmethod


class Document(ABC):
    """Абстрактный класс для классов разных видов документов."""
    @abstractmethod
    def show(self):
        pass


class ODFDocument(Document):
    def show(self):
        print('Open document format')


class MSOfficeDocument(Document):
    def show(self):
        print('MS Office document format')


class Application(ABC):
    @abstractmethod
    def create_document(self, type_of_wanted_doc):
        # параметризованный фабричный метод `Создание документа`
        pass


class MyAppWithFabricMetod(Application):
    """Фабричный метод: в зависимости от переданного типа ожидаемого документа, возвращает объект
    определенного класса."""
    def create_document(self, type_of_wanted_doc):
        if type_of_wanted_doc == 'odf':
            return ODFDocument()
        elif type_of_wanted_doc == 'doc':
            return MSOfficeDocument()


app = MyAppWithFabricMetod()
app.create_document('odf').show()  # Open document format
app.create_document('doc').show()  # MS Office document format


# Фабричный метод — это порождающий паттерн проектирования, который позволяет подклассам изменять создаваемый объект,
# в зависимости от контекста. Объединяя сущности в обобщенную абстракцию.

