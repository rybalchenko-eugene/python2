import csv
import re
import logging
import os
import argparse

# запуск из терминала, текущей папки например >>>py .\main.py Sorted

logging.basicConfig(filename='unsorted_letters.log.', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser(description='My first argument parser')
parser.add_argument('names', metavar='DirName', type=str, nargs=1, help='enter name for SortedDir')
args = parser.parse_args()
print(f'В скрипт передано: {args}')

dict_type = {
    'Security': ['парол', 'взлом', 'несанкционир', 'укра', 'похити', 'несанкционир', 'скам', 'мошенн', 'авториз'],
    'Refunds': ['возврат средств', 'отменить подписку', 'отключить подписк', 'вернуть',
                'отказаться', 'отменить', 'отписат', 'деньги'],
    'Troubleshooting': ['забыл пароль', 'не подходит пароль', 'сбой', 'проблем',
                        'ошибк', 'не работа', 'глюк', 'сбой', 'исправ', 'завис', 'медленно', 'неправильн'],
    'Account': ['забыл пароль', 'не подходит пароль', 'сбой', 'аккаунт', 'учетн', 'логин', 'аккаунт'],
    'Advertising and Collaboration': ['сотрудн', 'предлож', 'услуг', 'реклам', 'маркет', 'API', 'улучшить сервис',
                                      'привлечь', 'эффективн'],
    'Limits, Payments, Features': ['ограничен', 'Visa', 'Mastercard', 'платеж', 'paypal', 'лимит', 'оплат',
                                   'банковск', 'функционал', 'Bitcoin', 'продле', 'подписк', 'текст', 'бесплатн']
}

try:

    with open('user_support_letters.csv', 'r', newline='', encoding='utf-8') as f:
        max_group = 2  # количество групп для одного письма
        max_group1 = max_group

        storage: {str: [[]]} = dict.fromkeys(dict_type.keys(), '')
        # storage['Unsorted'] = ''
        for line in f:
            max_group = 2  # макс.количество групп для одного письма
            counter: {str: [[]]} = dict.fromkeys(dict_type.keys(), 0)  # счетчик совпадений
            format_line = line.lower()
            format_line = re.sub(r'[^\w\s]', '', format_line)

            for key in dict_type:
                for word in dict_type[key]:
                    num = format_line.count(str(word).lower())
                    if num > 0:
                        counter[key] = num  # заполняем счетчик попаданий

            while max_group > 0:
                max_val = 0
                for key in counter:
                    if counter[key] > max_val:
                        max_val = counter[key]
                        max_key = key
                if max_val != 0 and line not in storage[max_key]:
                    storage[max_key] += line  # добавляем письмо в соответствующую категорию с макс.числом совпадений
                    counter[max_key] = 0
                elif max_val == 0 and max_group == max_group1:  # если совпадений в первый раз не найдено,
                    # отправляем в несортированные
                    logger.warning(line)
                    break
                max_group -= 1
except FileNotFoundError:
    print('No such file, exit')
    exit(1)
name = args.names[0]
if not os.path.exists(f'./{name}'):
    os.mkdir(f'./{name}')
for key in storage:
    name2 = str(key).replace(' ', '_')
    name2 = name2.replace(',', '_')

    with open(f'./{name}/{name2}.csv','w', newline='\n', encoding='utf-8') as w:
        wr = csv.writer(w)
        line = str(storage[key]).split('\n')
        for item in line:
            wr.writerow([item])
    # print(f'{key}:\n{storage[key]}')
