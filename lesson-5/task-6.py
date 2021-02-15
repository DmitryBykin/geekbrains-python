# Задание 6
# 6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь,
# содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

def get_number(str):
    nums = ''
    for ch in str:
        if ch.isdigit():
            nums += ch
    return int(nums) if nums else None


subjects = {}
with open('data-6.txt', 'r') as f:
    for line in f:
        line_list = line.split(' ')
        subject = line_list[0]
        sum_hours = sum([get_number(hours) for hours in line_list[1:] if get_number(hours)])
        subjects.setdefault(subject, sum_hours)

print(subjects)
