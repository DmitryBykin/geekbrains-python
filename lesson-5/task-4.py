# Задание 4
# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.

numerals = {'Zero': 'Ноль', 'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре', 'Five': 'Пять',
            'Six': 'Шесть', 'Seven': 'Семь', 'Eight': 'Восемь', 'Nine': 'Девять', 'Ten': 'Десять'}

# 1 способ
with open('data-4_input.txt', 'r') as f_input, open('data-4_output.txt', 'w') as f_output:
    for line in f_input:
        numeral = line.split(' ')[0]
        line = line.replace(numeral, numerals[numeral])
        f_output.write(line)


# 2 способ
# with open('data-4_input.txt', 'r') as f_input, open('data-4_output.txt', 'w') as f_output:
#     for line in f_input:
#         line_list = line.split(' ')
#         numeral = line_list[0].capitalize()
#         f_output.write(numerals[numeral] + ' '.join(line_list[1:]))
