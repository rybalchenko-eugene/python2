# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
import datetime
from sys import argv
# Запускать с терминала
# вводи с датой типа:>>>  python date_check.py 12 12 2021


def check_date(input_date: list) -> bool:
    try:
        if len(input_date) == 1:
            day, month, year = input_date.split('/')
        else:
            day, month, year = input_date
    except:
        return False
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        return False
    return True

if __name__ == '__main__':
    # print(check_date([12,12,2011]))
    # print(check_date(['12', '12', '2011']))
    # print(check_date('21/02/2023'))
    print(argv)
    if len(argv) == 4:
        print(check_date(argv[1:]))
    else:
        print('Запускать с терминала, с датой типа: >>> python date_check.py 12 12 2021')
