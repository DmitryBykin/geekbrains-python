# задание 2
# Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open('data-2.txt', 'r') as f:
    strings = 0
    for line in f:
        strings += 1
        print(f'Слов в строке {strings}: {len(line.split(" "))}')
print(f'Всего строк в файле: {strings}')
