# Задание 6
# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите внимание, что создаваемый цикл
# не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.

from itertools import count, cycle


def int_nums(start_value=1, max_value=10):
    for value in count(start_value):
        if value > max_value:
            break
        yield value


def cycle_list(cycle_values, max_full_cycles=5):
    cycles = 0
    for el in cycle(cycle_values):
        if cycles // len(cycle_values) >= max_full_cycles:  # завершение после прохода последнего полного цикла
            break
        cycles += 1
        yield el


for el in int_nums(10, 15):
    print(el)

for el in cycle_list([1, 2, 3, 4]):
    print(el)
