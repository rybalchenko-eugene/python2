class Matrix:
    """
    Класс Матрица. Имеет методы для:
    ○ вывода на печать,
    ○ сравнения,
    ○ сложения,
    ○ *умножения матриц
    """

    def __init__(self, data: [[int]]):
        self.data = data

    # проверка валидности данных
    def __new__(cls, data):
        inst = super().__new__(cls)
        first_len = len(data[0])
        for i in data:
            if len(i) != first_len:
                return None
        return inst

    def __add__(self, other):
        # проверки на валидность
        if self is None or other is None:
            return None
        if len(self.data) != len(other.data):
            return None

        new_matr = []
        for r in range(len(self.data)):
            if len(self.data[r]) != len(other.data[r]):
                return None
            new_line = []
            for c in range(len(self.data[r])):
                new_line.append(self.data[r][c] + other.data[r][c])
            new_matr.append(new_line)
        return Matrix(new_matr)

    def __eq__(self, other):
        # if len(self.data) != len(other.data):  Поэлементное сравнение тут не нужно
        #     return False
        # new_matr = []
        # for r in range(len(self.data)):
        #     if len(self.data[r]) != len(other.data[r]):
        #         return False
        #     new_line = []
        #     for c in range(len(self.data[r])):
        #         if self.data[r][c] != other.data[r][c]:
        #             return False
        #     new_matr.append(new_line)
        # return True
        if self.data != other.data:
            return False
        return True

    def __lt__(self, other):
        if self.data < other.data:
            return False
        return True

    def __gt__(self, other):
        if self.data < other.data:
            return False
        return True

    # и т.п методы

    def __mul__(self, other):
        # проверки на валидность
        if self is None or other is None:
            return None
        if len(self.data[0]) != len(other.data):
            return None

        res = [[0 for x in range(len(other.data))] for _ in range(len(self.data))]
        # explicit for loops
        for i in range(len(self.data)):
            for j in range(len(other.data[0])):
                for k in range(len(other.data)):
                    # resulted matrix
                    res[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(res)

    def __str__(self):
        print(*self.data, sep='\n')  # можно ли сделать такой вывод вместо return ?
        return '----'

    def __repr__(self):
        return f'Matrix({self.data})'


if __name__ == '__main__':
    data1 = [[12, 5, 27], [1, 5, 43], [-45, 2, -99], [7, 3, -8]]
    data2 = [[1, 32, 7], [-11, 8, -3], [5, 20, 9], [17, 34, -52]]
    data3 = [[12, 5, 27], [1, 5, 43], [-45, 2, -99], [7, 3, -8]]  # копия data1
    wrong = [[5, 27], [1, 5, 43], [-45, 2, -99], [7, 3, -8]]  # проверка валидности
    data4 = [[12, 5, 27, -4], [1, 5, 43, 1], [-45, 2, -99, 0]]  # для перемножения

    m1 = Matrix(data1)
    m2 = Matrix(data2)
    m3 = Matrix(data3)
    wr = Matrix(wrong)
    m4 = Matrix(data4)

    print(f'{m1 + m2 = };\n{m2 + wr = }')
    print(f'{m1 == m2 = }\n{m1 == m3 = }')
    print(f'{m1 > m2 = }')
    print('m4 * m1 = ', m4 * m1, sep='\n')

