# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

text_path = r'C:\Users\ren\Documents\Private\Lessons\Python2\Lesson 24\task 1.py'


def parser(path: str):
    *path, file = path.split('\\')
    name, ext = file.split('.')
    return "\\".join(path), name, ext


print(parser(text_path))
print(f'path = {parser(text_path)[0]}')
# disk, *_ = text_path.split('\\')
# print(f'disk = {disk}')
