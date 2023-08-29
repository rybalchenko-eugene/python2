# Нахождение корней квадратного уравнения
# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
import csv
import math
from random import randint
import json


def saver_json(func: callable) -> callable:
    """
    Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
    """
    def wrapper2(filename: str):
        res_dict = func(filename)

        with open('data_res.json', 'w') as f:
            print('Saving result to json-file')
            json.dump(res_dict, f, indent=2)

    return wrapper2


def from_csv_sqrt(func: callable) -> callable:
    """
    Декоратор, запускающий функцию нахождения корней
    квадратного уравнения с каждой тройкой чисел из csv файла.
    """
    def wrapper1(filename: str):
        res_dict = {}
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for line in list(reader):
                print(line)
                a, b, c = line
                res = func(int(a), int(b), int(c))
                print(res)
                res_dict[a + ' ' + b + ' ' + c] = res
            return res_dict

    return wrapper1


@saver_json
@from_csv_sqrt
def sqrt_func(a: int, b: int, c: int) -> tuple:
    """
    Нахождение корней квадратного уравнения
    Отрицательный дискрминант не имеет решения (None)
    """
    d = b ** 2 - 4 * a * c
    # убираем отрицательный дискриминант и а=0
    if d >= 0 and a != 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        return x1, x2
    else:
        return None


def gen_csv(filename: str, size=200):
    """
    Генерация csv файла с тремя случайными числами в каждой строке.
    Параметр - количество строк.
    """
    # генерация случайных чисел в список списков
    line = 3
    llevel = -100
    ulevel = 100
    lst = []
    for _ in range(size):
        lst1 = []
        for _ in range(line):
            lst1.append(randint(llevel, ulevel))
        lst.append(lst1)

    # запись в csv-файл
    with open(filename, 'w', newline='') as fw:
        writer = csv.writer(fw, delimiter=',', dialect='excel')
        writer.writerows(lst)


if __name__ == '__main__':
    filename = 'data.csv'
    # генерируем исходники
    gen_csv(filename)

    # вызов функции с двумя декораторами
    sqrt_func(filename)
