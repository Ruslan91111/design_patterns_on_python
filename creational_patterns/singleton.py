"""Пример паттерна одиночка(singleton)"""


class Singleton:
    def __new__(cls):
        # Перед созданием нового объекта класса, проверяем, а нет ли уже одного объекта этого класса.
        # Если есть, то не даем создать новый объект, а возвращаем существующий.
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance


s = Singleton()
print(id(s))
print(s)

b = Singleton()  # Не создаст новый объект, а вернет объект с id, на который ссылается объект s.

print(id(b))
print(b)

print(s is b)  # Покажет True


# Гарантирует, что у класса есть только один экземпляр!
# Предоставляет глобальную точку доступа.
