# Задание 7
# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
#
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

firms = {}
average_profit = {}
total_profit = amount_profit_companies = 0

with open('data-7.txt', 'r') as f:
    for line in f:
        line_list = line.split(' ')
        company_name, company_profit = line_list[0], float(line_list[2]) - float(line_list[3])
        if company_profit > 0:
            total_profit += company_profit
            amount_profit_companies += 1

        firms.setdefault(company_name, company_profit)

    average_profit.setdefault('average_profit', total_profit / amount_profit_companies)

print(firms)
print(average_profit)

with open('data-7.json', 'w') as f:
    json.dump([firms, average_profit], f)

with open('data-7.json', 'r') as f:
    data = json.load(f)
    print(data[1]['average_profit'])