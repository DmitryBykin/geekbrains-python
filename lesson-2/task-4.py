# Задание 4
# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

input_str = input('Введите строку: ')
words = input_str.split(' ')
for ind, word in enumerate(words):
    print(f'{ind} {word[:10]}')
