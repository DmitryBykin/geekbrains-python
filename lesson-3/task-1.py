# Задание 1
# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def check_not_zero(y):
    return bool(y)


def divide_numbers(x, y):
    return x / y


x = float(input('Введите число 1 (делимое): '))
y = float(input('Введите число 2 (делитель): '))

if check_not_zero(y):
    result = divide_numbers(x, y)
    print(f'Результат {x} / {y} = {result}')
else:
    print('На ноль делить нельзя')
