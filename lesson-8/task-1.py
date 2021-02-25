# Задание 1
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки
# формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу полученной
# структуры на реальных данных.

class Date:

    @classmethod
    def __init__(cls, date_str):
        cls.date_str = date_str

    @classmethod
    def get_date(cls):
        cls.day, cls.month, cls.year = map(int, (item for item in cls.date_str.split('-')))

    @staticmethod
    def validate_date():
        if not 0 < Date.day < 32:
            print('День не может быть меньше 1 или больше 31')
            return False

        if not 0 < Date.month < 13:
            print('Месяц не может быть меньше 1 или больше 12')
            return False

        if not 1799 < Date.year < 2051:
            print('Год не может быть меньше 1800 или больше 2050')
            return False

        return True

    @classmethod
    def __str__(cls):
        return f'День {cls.day}: месяц {cls.month}, год {cls.year}'


date = Date('32-02-2100')
date.get_date()
if date.validate_date():
    print(date)

date = Date('11-00-2020')
date.get_date()
if date.validate_date():
    print(date)

date = Date('24-02-2021')
date.get_date()
if date.validate_date():
    print(date)
