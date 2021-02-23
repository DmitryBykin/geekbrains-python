# Задание 1
# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        s = ''
        for row in self.matrix:
            for col in row:
                s += f'{col:>3}'
            s += '\n'
        return s

    def __add__(self, other):
        matrix = []
        for ind_row, row in enumerate(self.matrix):
            cur_row = []
            for ind_col, col in enumerate(row):
                cur_row.append(col + other.matrix[ind_row][ind_col])
            matrix.append(cur_row)

        return Matrix(matrix)

    # умножение матриц (дополнительно для себя)
    def __mul__(self, other):
        if len(self.matrix[0]) != len(other.matrix):
            print('Перемножение матриц невозможно.')
            print('Число столбцов первой матрицы должно быть равно числу строк второй')
            return

        other_transposed = list(zip(*other.matrix))
        matrix = []
        for row_self in self.matrix:
            cur_row = []
            for row_other in other_transposed:
                cur_row.append(sum(list(map(lambda x: x[0] * x[1], zip(row_self, row_other)))))
            matrix.append(cur_row)

        return Matrix(matrix)

        # вариант 2
        # matrix = []
        # for row in range(len(self.matrix)):
        #     cur_row = []
        #     for col in range(len(other.matrix[0])):
        #         sum = 0
        #         for i in range(len(other.matrix)):
        #             sum += self.matrix[row][i] * other.matrix[i][col]
        #         cur_row.append(sum)
        #     matrix.append(cur_row)

        # return Matrix(matrix)


m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

print(f'Матрица 1: \n{m1}')
print(f'Матрица 2: \n{m2}')
print(f'Матрица 1 + 2: \n{m1 + m2}')
print(f'Матрица (2x2) * (2x2): \n{m1 * m2}')

m1 = Matrix([[1, 2], [3, 4], [6, 7]])
m2 = Matrix([[7], [9]])
print(f'Матрица (3x2) * (2x1): \n{m1 * m2}')

m1 = Matrix([[1, 2, 3]])
m2 = Matrix([[1, 2], [3, 4], [6, 7]])
print(f'Матрица (1x3) * (3x2): \n{m1 * m2}')

m1 = Matrix([[1, 2, 3]])
m2 = Matrix([[1, 2], [3, 4]])
print(f'Матрица (1x3) * (2x2): \n{m1 * m2}')
