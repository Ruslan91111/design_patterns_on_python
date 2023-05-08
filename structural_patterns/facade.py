class Paper:
    def __init__(self, count):
        """Количество имеющейся бумаги."""
        self._count = count

    def get_count(self):
        """Вывести количество бумаги в наличии."""
        return self._count

    def take_paper_and_print(self, text):
        """Взять бумагу для печати"""
        if self._count > 0:
            self._count -= 1
            print(text)


class Printer:
    def error(self, msg):
        print('Ошибка: %s' % msg)

    def print_something(self, paper, text):
        if paper.get_count() > 0:
            paper.take_paper_and_print(text)
        else:
            self.error('Бумага закончилась')


class Facade:
    """Класс - 'Фасад', получает объекты бумаги и принтера """
    def __init__(self):
        self._printer = Printer()
        self._paper = Paper(1)

    def print_something_for_user(self, text):
        self._printer.print_something(self._paper, text)


facade = Facade()
facade.print_something_for_user('Hello world!') # Hello world!
facade.print_something_for_user('Hello world!') # Ошибка: Бумага закончилась


# Фасад — структурный паттерн проектирования, позволяющий дать интерфейс более высокого уровня к сложной системе.
# В отличии от адаптера, используется новый интерфейс.
# Большой минус в том, что в данной концепции, фасад может стать godlike, связанным со всей системой.
# Иногда фасад превращают в синглтон, т.к. обычно нужен всего 1 фасад.
