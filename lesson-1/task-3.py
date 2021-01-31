# задание 3
# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

input_number = input('Ведите число (n): ')
sum = int(input_number) + int(input_number * 2) + int(input_number * 3)
print(f'Сумма чисел n+nn+nn: {sum}')


