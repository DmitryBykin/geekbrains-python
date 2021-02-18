# Задание 5
# 5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название)
# и метод draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка),
# Pencil (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из
# классов методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный
# метод для каждого экземпляра.

class Stacionery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stacionery):
    def draw(self):
        print(f'Рисует "{self.title}"')


class Pencil(Stacionery):
    def draw(self):
        print(f'Рисует "{self.title}"')


class Handle(Stacionery):
    def draw(self):
        print(f'Рисует "{self.title}"')


stacionery = Stacionery('канцелярская принадлежность')
pen = Pen('ручка гелевая')
pencil = Pencil('цветной карандаш')
handle = Handle('черный маркер')

stacionery.draw()
pen.draw()
pencil.draw()
handle.draw()
