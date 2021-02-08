# Задание 5
# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел, разделенных
# пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
# чисел к полученной ранее сумме и после этого завершить программу.

def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

total_sum = 0
input_end = False
while not input_end:
    numbers_list = input('Введите числа через пробел (Q/q - выход): ').split()
    numbers = []
    for item in numbers_list:
        if item.upper() == 'Q':
            input_end = True
            break
        elif is_number(item):
            numbers.append(float(item))

    total_sum += sum(numbers)
    print(f'Сумма чисел= {total_sum}')
