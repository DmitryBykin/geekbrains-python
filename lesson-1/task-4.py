# Задание 4
# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положительное число: '))

divider = 10
max_digit = number % divider

while number // divider != 0:
    divider *= 10
    cur_digit = int((number % divider) // (divider / 10))
    if cur_digit > max_digit:
        max_digit = cur_digit

print(f'Максимальная цифра: {max_digit}')
