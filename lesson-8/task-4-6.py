# Задание 6
# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.

class Storage:
    N = 100

    @staticmethod
    def print_divider():
        print('-' * Storage.N)

    class Orgtechnics:

        def __init__(self, title):
            self.title = title
            self.amount = {}

        def __str__(self):
            return f'{self.title}'

        def check_params(f):
            def wrapper(self, *args):
                if not isinstance(args[0], int):
                    print('Количество должно быть целым числом <int>')
                    print('Перемещение или поступление товара нас склад не проведено')
                    Storage.print_divider()
                    return
                for par in args[1:]:
                    if not isinstance(par, str):
                        print('Департамент должныть быть строковым ')
                        print('Перемещение или поступление товара на склад не проведено')
                        Storage.print_divider()
                        return
                return f(self, *args)

            return wrapper

        @check_params
        def to_storage(self, amount, department='основной склад'):
            """
            Приход на склад

            :param amount: количество единиц техники
            :param department: в какое подразделение (по умолчанию 'основной склад')
            :return:
            """

            print(f'Поступление на склад "{self.title}", количество: {amount}')
            try:
                self.amount[department] += amount
            except KeyError:
                self.amount.setdefault(department, amount)

        @check_params
        def move_equipment(self, amount, from_department, to_department):
            """
            Перемещение между подразделениями (в том числе с основного склада)

            :param amount: количество единиц техники
            :param from_department: из какого подразделения
            :param to_department: в какое подразделение
            :return:
            """

            print(f'Перемещение оборудования "{self.title}" "{from_department}"->"{to_department}" ')
            try:
                if self.amount[from_department] >= amount:
                    self.amount[from_department] -= amount
                    try:
                        self.amount[to_department] += amount
                    except KeyError:
                        self.amount.setdefault(to_department, amount)
                else:
                    print(f'Недостаточно оборудования в подразделении "{from_department}" для перемещения')
                    Storage.print_divider()
            except KeyError:
                print(f'Оборудование {self.title} отсутствует в подразделении "{from_department}"')
                print('Перемещение невозможно')
                Storage.print_divider()

        @property
        def total_items(self):
            return f'Остаток "{self.title}": {self.amount}'

    class Printer(Orgtechnics):
        def __init__(self, title, size, print_speed):
            super().__init__(title)
            self.size = size
            self.print_speed = print_speed

        def __str__(self):
            return f'{self.title}, формат {self.size}'

    class Scaner(Orgtechnics):
        def __init__(self, title, scan_speed):
            super().__init__(title)
            self.scan_speed = scan_speed

    class Xerox(Orgtechnics):
        def __init__(self, title, copy_speed):
            super().__init__(title)
            self.copy_speed = copy_speed


printer = Storage.Printer('Принтер HP LaserJet', 'A3', 22)
print(printer)
printer.to_storage(3)
print(printer.total_items)
Storage.print_divider()

scaner = Storage.Scaner('Сканер Epson', 5)
print(scaner)
scaner.to_storage(5)
print(scaner.total_items)
Storage.print_divider()

xerox = Storage.Xerox('Копир Kyocera', 17)
xerox.to_storage(1)
print(xerox)
print(xerox.total_items)
Storage.print_divider()

printer.move_equipment(1, 'основной склад', 'бухгалтерия')
print(printer.total_items, end='\n\n')

printer.move_equipment(1, 'основной склад', 'бухгалтерия')
print(printer.total_items, end='\n\n')

printer.move_equipment(1, 'основной склад', 'Цех № 123')
print(printer.total_items, end='\n\n')

printer.move_equipment(1, 'основной склад', 'Цех № 123')
print(printer.total_items, end='\n\n')

xerox.move_equipment(1, 'основной склад', 'отдел продаж')
print(xerox.total_items, end='\n\n')

scaner_2 = Storage.Scaner('Epson A3', 2)
scaner_2.move_equipment(2, 'основной склад', 'цех № 555')

scaner_2.to_storage(3)
scaner_2.move_equipment(2, 'основной склад', 'цех № 555')

scaner_2.to_storage('10')
printer.move_equipment('1', 'основной склад', 'отдел продаж')
Storage.print_divider()

printer.move_equipment(1, 'основной склад', 555)
