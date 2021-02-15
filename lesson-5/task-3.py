# Задание 3
# Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов
# (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open('data-3.txt', 'r') as f:
    lines = f.readlines()

employers_less_20k = [line.split(' ')[0] for line in lines if float(line.split(' ')[1]) < 20000]
print(f'Сотрудники с зарплатой менее 20 000: {" ".join(employers_less_20k)}')

employers_salaries = [float(line.split(' ')[1]) for line in lines]
print(f'Средняя зарплата сотрудников: {sum(employers_salaries) / len(employers_salaries)}')
