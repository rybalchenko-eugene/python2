# ЗАДАЧА 2: Напишите функцию группового переименования файлов. Она должна:
# - принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# - принимать параметр количество цифр в порядковом номере.
# - принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# - принимать параметр расширение конечного файла.
# - принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
#
# Пример:
# rename(wanted_name = "video", count_nums=3, extension_old=".txt", extension_new=".csv", diapazon=[3, 6])
# foto_2002.txt -> o_20video001.csv


import os
import IO_module as io


def files_rename(wanted_name: str, count_nums: int, extension_old: str, extension_new: str, diapazon=[3, 6]):
    count = 1
    os.chdir('TestDir')
    for file in os.listdir():
        try:
            old_name, ext = file.split('.')
        except:
            continue

        if ext == extension_old[1:]:
            new_name = old_name[diapazon[0]:diapazon[1]] + wanted_name + f'{count:0{count_nums}d}' + extension_new
            print(file, '->', new_name)
            os.rename(file, new_name)
            count += 1


files_rename('_ubuntu', 4, '.doc', '.txt', [0, 2])

# ЗАДАЧА 3:Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

p = 'C:\\Users\\ren\\Documents\\Private\\Lessons\\Python2\\Lesson 27\\TestDir'

io.file_sorter(p)
