from functools import wraps


def decorator(func):
    # @wraps - придает сигнатуру функции.
    @wraps(func)
    # функция - обертка
    def wrapper(*args, **kwargs):
        # Добавляемый функционал перед вызовом декорируемой функции.
        print('doing something')
        # Переменной присваиваем результат вызова декорируемой функции.
        result = func(*args, **kwargs)
        # Добавляемый функционал после вызова декорируемой функции.
        print('doing something after')
        # Возвращаем переменную с вызовом декорируемой функции.
        return result

    # Возвращает функцию - обертку без вызова.
    return wrapper


# Синтаксический сахар.
@decorator
def som():
    print('a' * 3 + '!')


print(som)
# <function som at 0x7f5593ad8940>
# Такой вид благодаря @wraps, который добавил сигнатуру функции
# Без wraps в декораторе будет выглядеть:
# <function decorator.<locals>.wrapper at 0x7fe42b038940>


# Вызвать функцию, украшенную декоратором.
som()
print("it's was first")

som2 = decorator(som)
som2()
print("it's was second")


# Написать декоратор, чтобы можно было пробросить аргумент
# в сам декоратор.

# Обернули в еще одну функцию, принимающую аргумент.
def outer(a=1):
    # Сам декоратор, принимающий в качестве аргумента функцию.
    def decorator(func):
        # Чтобы декорируемая функция, могла принимать аргумента,
        # нужно эти аргументы указать и в декорируемой функции.
        def wrapper(*args, **kwargs):
            print('doing something')
            res = func(*args, **kwargs)
            print('doing something after')
            # Вернули переменную
            return res
        # Вернули обертку
        return wrapper
    # Вернули декоратор.
    return decorator


@outer(123)   # Синтаксический сахар, в который уже можно передавать аргументы.
def som(x):
    print(x * 3)

som(2)
print("it's was third")

