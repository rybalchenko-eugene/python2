# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие вещи
# влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.


import copy

items = {'лодка': 10.1, 'палатка': 10, 'котел': 2, 'топор': 3, 'стулья': 7, 'стол': 4, 'горелка': 1, 'удочки': 1.5,
         'тент': 2.3, 'сеть': 4.1, 'мотор': 5, 'алкоголь': 4.9}

VOLUMEPACK = 25


def max_weight(items: dict) -> str:
    res = None
    for item in items:
        max = 0
        if items[item] > max:
            max = items[item]
            res = item
    return res


# начинаем с одной вещи по очереди
for i1 in items:

    # перебираем последовательно вторую вещь
    for i2 in items:
        rest_items = copy.deepcopy(items)
        total_weight = 0
        pack = []
        if total_weight + items.get(i1) <= VOLUMEPACK:
            total_weight += items.get(i1)
            pack.append(i1)
        rest_items.pop(i1)

        if total_weight + items[i2] <= VOLUMEPACK and i2 not in pack:
            total_weight += items[i2]
            pack.append(i2)
            rest_items.pop(i2)

            # добираем первое попавшееся из имеющегося
            while total_weight < VOLUMEPACK and rest_items != {}:
                new_item = rest_items.popitem()[0]
                if total_weight + items[new_item] <= VOLUMEPACK and new_item not in pack:
                    total_weight += items[new_item]
                    pack.append(new_item)

            print(pack, total_weight)

