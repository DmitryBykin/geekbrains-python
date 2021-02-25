# Задание 2
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.

class ZeroDivException(Exception):

    def __init__(self, msg):
        self.msg = msg


def div_func(x, y):
    try:
        if y == 0:
            raise ZeroDivException('деление на ноль!')
        else:
            return x / y
    except ZeroDivException as err:
        print(err)


print(div_func(10, 2))
print(div_func(10, 0))
print(div_func(10, -2))