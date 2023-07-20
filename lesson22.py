import sys
import math
import fractions

# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
## порядковый номер начиная с единицы
# значение # адрес в памяти # размер в памяти # хэш объекта # результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный Добавьте в список повторяющиеся элементы и сравните на результаты.



data = [12, 'Text string', {1: 'trew', 2: 123, 3: 12.33}, [1,5,2,'23ff'], 12.34, (123, 43,213,11.2), 'Text string']
for item in data:
    print(f'Pos.{data.index(item)+1}: {item}, {type(item) = }, id:{id(item)}, size:{sys.getsizeof(item)}')
    if not isinstance(item, dict) and not isinstance(item, list):
        print(f'{hash(item) = }')
    if isinstance(item, int):
        print('целое число')


#  Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

check = False
BASE = 16
while not check:
    num = input('№1 Введите число для перевода в 0x: ')
    if num.isnumeric():
        check = True
    else:
        print('Неверный ввод, ')
print('Встроенная функция переводит', num, 'как ' ,hex(int(num)))
num = int(num)
convert_num = ''
while num:
    letter = num % BASE
    match letter:
        case 10:
            letter = 'A'
        case 11:
            letter = 'B'
        case 12:
            letter = 'C'
        case 13:
            letter = 'D'
        case 14:
            letter = 'E'
        case 15:
            letter = 'F'
    convert_num = str(letter) + convert_num
    num //= BASE
print('написанная программа переводит ввод как 0x:' , convert_num, sep="")

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем. Программа должна
# возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

fract1 = input('\n №3 Введите первую дробь вида A/B: ')
fract2 = input('Введите вторую дробь вида C/D: ')
list1 = fract1.split('/')
list2 = fract2.split('/')
# проверки на корректный ввод не проводим
# умножение

num1 = int(list1[0])*int(list2[0])
div1 = int(list1[1])*int(list2[1])
nod = math.gcd(num1, div1)
print(f'произведение дробей = {int(num1/nod)}/{int(div1/nod)}')
# сложение
num2 = int(list1[0])*int(list2[1]) + int(list2[0])*int(list1[1])
div2 = int(list1[1])*int(list2[1])
nod = math.gcd(num2, div2)
print(f'сложение дробей = {int(num2/nod)}/{int(div2/nod)}')
# проверка
fr1 = fractions.Fraction(int(list1[0]), int(list1[1]))
fr2 = fractions.Fraction(int(list2[0]), int(list2[1]))
print('Умножение встроенным модулем Fractions = ', (fr1 * fr2))
print('Сложение встроенным модулем = ', (fr1 + fr2))