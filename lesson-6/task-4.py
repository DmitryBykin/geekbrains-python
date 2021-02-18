# Задание 4
# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
# is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('машина поехала')

    def stop(self):
        print('машина остановилась')

    def turn(self, direction):
        print(f'машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        Car.__init__(self, speed, color, name, is_police=True)


town_car = TownCar(65, 'зеленый', 'Lada')
print(f'Модель: {town_car.name}, скорость: {town_car.speed}, цвет: {town_car.color}, полицейский: {town_car.is_police}')
town_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('влево')
town_car.turn('вправо')

work_car = WorkCar(50, 'красный', 'Камаз')
print(f'Модель: {work_car.name}, скорость: {work_car.speed}, цвет: {work_car.color}, полицейский: {work_car.is_police}')
work_car.show_speed()

work_car = WorkCar(20, 'желтый', 'Трактор')
print(f'Модель: {work_car.name}, скорость: {work_car.speed}, цвет: {work_car.color}, полицейский: {work_car.is_police}')
work_car.show_speed()

police_car = PoliceCar(75, 'синий', 'УАЗ')
print(f'Модель: {police_car.name}, скорость: {police_car.speed}, цвет: {police_car.color}, полицейский: {police_car.is_police}')
police_car.show_speed()
