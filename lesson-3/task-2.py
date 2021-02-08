# Задание 2
# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def print_user_data(**kwargs):
    for feature, value in kwargs.items():
        print(f'{feature}:{value} ', end='')


features = ['имя', 'фамилия', 'год рождения', 'город проживания', 'email', 'телефон']
user_data = {}
for feature in features:
    prop = input(f'Введите значение свойства "{feature}": ')
    user_data[feature] = int(prop) if feature == 'год рождения' else prop

print_user_data(**user_data)
