# Задание 7
# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
# реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:

    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im

    def __add__(self, other):
        return Complex(self.Re + other.Re, self.Im + other.Im)

    def __mul__(self, other):
        return Complex(self.Re * other.Re - self.Im * other.Im, self.Im * other.Re + self.Re * other.Im)

    def __str__(self):
        return f'{self.Re}+{self.Im}i'


c1 = Complex(3, 4)
c2 = Complex(1, 2)

print(c1 + c2)
print(c1 * c2)