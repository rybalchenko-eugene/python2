# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.

import os
import json
import csv
import pickle


def get_dir_size(dir_path: str) -> int:
    size = 0
    # get size
    for ele in os.scandir(dir_path):
        size += os.path.getsize(ele)
    return size


def ll(directory: str) -> None:
    total_lst = []
    for dir_path, dir_name, file_name in os.walk(directory):
        curdir_lst = {}
        curdir_lst['path'] = dir_path
        curdir_lst['parent'] = os.path.dirname(dir_path)
        curdir_lst['Files/size'] = {file: os.path.getsize(f'{dir_path}/{file}') for file in file_name}
        curdir_lst['Directory/size'] = {dir: get_dir_size(f'{dir_path}/{dir}') for dir in dir_name}
        total_lst.append(curdir_lst)

    with open('list_dir.json', 'w') as fj:
        json.dump(total_lst, fj, indent=2)

    with open('list_dir.csv', 'w', encoding='utf-8', newline='') as fc:
        csv_writer = csv.DictWriter(fc, dialect='excel-tab', delimiter='|',
                                    fieldnames=['path', 'parent', 'Files/size', 'Directory/size'])
        csv_writer.writeheader()
        for item in total_lst:
            csv_writer.writerow(item)

    with open('list_dir.pickle', 'wb') as fp:
        pickle.dump(total_lst, fp)


if __name__ == '__main__':
    ll('..')
