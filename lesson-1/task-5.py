# Задание 5
# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

proceeds_amount = float(input('Введите сумму выручки, руб.: '))
expenses_amount = float(input('Введите сумму издержек, руб.: '))

if proceeds_amount > expenses_amount:
    print('Фирма работает с прибылью')
    profitability_amount = ((proceeds_amount - expenses_amount) / proceeds_amount) * 100  # рентабельность в процентах
    print(f'Рентабельность: {profitability_amount:.2f}%')
    employers_count = int(input('Введите численность сотрудников: '))
    profitability_per_employer = (proceeds_amount - expenses_amount)/employers_count
    print(f'Прибыльность на одного сотрудника, руб.: {profitability_per_employer:.2f}')
else:
    print('Фирма работает с убытками')
