"""
Задание. Создайте класс студента.
- Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
- Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
- Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
- Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взя
"""
import csv
import statistics


class CheckName:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        if self.validate(value):
            setattr(instance, self.param_name, value)
        else:
            print("Не могу создать такое имечко")

    def validate(self, name: str):
        if not name.istitle():
            return False
        if not name.isalpha():
            return False
        return True


class Std:
    first_name = CheckName()
    last_name = CheckName()

    def check_num(self, bottom, up, value: []):
        for i in value:
            if i < bottom or i > up:
                return False
        return True

    def __init__(self, first_name, last__name, **kwargs):
        self.first_name = first_name
        self.last_name = last__name

        with open('table.csv', 'r', encoding='utf-8-sig', newline='') as f:
            reader = csv.DictReader(f, delimiter=';')
            self.subj = {i: [] for i in reader.__next__() if i != "Fullname"}
        for k, mark in kwargs.items():
            if k in self.subj.keys() and len(mark) > 0:
                if len(mark) == 2:
                    if self.check_num(2, 5, mark[0]) and self.check_num(0, 100, mark[1]):
                        self.subj[k] = mark
                    else:
                        print('Неверный формат оценки')
                else:
                    print('Неверный формат оценки/тестов')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return f'Полное имя:{self.full_name} \nПредметы: {self.subj.keys()} \nУспеваемость:{self.avr_marks()}'

    def avr_marks(self):
        """
        экземпляр сообщает средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взя
        """
        len = tmp = 0
        res = ''
        for k, mark in self.subj.items():

            if mark != []:
                tmp += statistics.mean(mark[0])
                res += f'\nСредний тест по предмету {k}:{statistics.mean(mark[1])}'
                len += 1
        if len > 0:
            res += f'\nСредняя оценка по предметам:{tmp / len}'
        else:
            res = 'Оценок еще нет'
        return res


if __name__ == '__main__':
    std0 = Std('Петр', 'Петрович', Физика=[[5, 5, 3], [50, 60]])
    print(std0)

    std1 = Std('Иван', 'Морозов', Математика=[[5, 3, 4], [50, 90]], Физика=[[5, 2, 3], [65, 90]],
               Украинский=[3, 5])
    print(std1.full_name)
    print(std1)

    name2 = 'Аббобаин2'
    std1.first_name = name2

