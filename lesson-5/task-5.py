# Задание 5
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

MAX_NUM_COUNT = 10
MAX_NUMBER = 100

numbers = []
for _ in range(MAX_NUM_COUNT):
    numbers.append(random.randint(0, MAX_NUMBER))

numbers = list(map(str, numbers))
with open('data-5.txt', 'w') as f:
    f.write(' '.join(numbers))

with open('data-5.txt', 'r') as f:
    numbers = f.readline().split(' ')

print(f'Сумма чисел в файле: {sum(list(map(int, numbers)))}')
