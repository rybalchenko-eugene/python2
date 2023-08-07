# Количество строк и имя файла передаются как аргументы функции
import random
import os

UPPER = 1000
LOWER = -1000


def num_gen(number, filename):
    with open(f'Lesson 27/TestDir/{filename}', 'w', encoding='utf-8') as f:
        while number != 0:
            num1 = random.randint(LOWER, UPPER)
            num2 = random.uniform(LOWER, UPPER)
            f.write(f'{num1}|{num2}\n')
            number -= 1


# num_gen(10, 'ntuvertu_new001.ab')


def name_gen(number, filename):
    with open(f'Lesson 27/TestDir/{filename}', 'a', encoding='utf-8') as f:
        while number != 0:
            word = ''
            for i in range(1, random.randint(5, 8)):
                word += chr(random.randint(98, 122))
            f.write(word.capitalize() + '\n')
            print(word.capitalize())
            number -= 1


# name_gen(10, 'ntuvertu_new002.ab')

def parser(filename1, filename2):
    with open(f'Lesson 27/TestDir/{filename1}', 'r', encoding='utf-8') as f1, \
            open(f'Lesson 27/TestDir/{filename2}', 'r', encoding='utf-8') as f2, \
            open(f'Lesson 27/TestDir/result.txt', 'w', encoding='utf-8') as f3:

        for line in f1:
            num1, num2 = line.split('|')
            res = int(num1) * float(num2)
            if res < 0:
                res = -res
            else:
                res = round(res, 0)
            name = f2.readline()
            f3.write(str(res) + ' ' + name.upper())


# parser('ntuvertu_new001.ab', 'ntuvertu_new002.ab')


def file_sorter(path_dir):
    video_types = ['mpeg4', 'mov', 'ps', 'ab']
    audio_types = ['mp3', 'flak', 'mid']
    doc_types = ['txt', 'doc']
    if os.path.isdir(path_dir):
        os.chdir(path_dir)

        for file in os.listdir():
            try:
                name, ext = file.split('.')
            except:
                continue
            if ext in video_types:
                if not os.path.isdir("Video"):
                    os.mkdir("Video")
                os.replace(file, os.path.join(os.getcwd(), 'Video', file))
            if ext in doc_types:
                if not os.path.isdir("Docs"):
                    os.mkdir("Docs")
                os.replace(file, os.path.join(os.getcwd(), 'Docs', file))
            if ext in audio_types:
                if not os.path.isdir("Audio"):
                    os.mkdir("Audio")
                os.replace(file, os.path.join(os.getcwd(), 'Audio', file))
    else:
            print('No such directory')


if __name__ == '__main__':
    file_sorter('TestDir')

