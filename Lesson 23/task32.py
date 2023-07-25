# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей. Ответьте на вопросы:
# * Какие вещи взяли все три друга
# * Какие вещи уникальны, есть только у одного друга
# * Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# * Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

items = {'John': ('лодка', 'стол', 'удочка', 'стул', 'котел', 'спички', 'карта'),
         'Simon': ('стол', 'горелка', 'удочка'),
         'Mario': ('тент', 'сеть', 'мотор', 'стул'),
         'Peterulya': ('стол', 'горелка', 'удочка', 'тетрадь', 'пиво')}

big_set = set()

for key in items:
    # все вещи
    big_set = big_set.union(items[key])

print(f'Все взятые вещи - {big_set}')


for key in items:
    uniq_set = set(items[key])
    for key2 in items:
        if key != key2:
            uniq_set = uniq_set.difference(items[key2])
    print(f'Г-ну {key} принадлежат уникальные вещи: {uniq_set}')

common_set = set()
for key in items:
    one_set = set(items[key])
    for key2 in items:
        if key != key2:
            common_set = common_set.union(one_set.intersection(items[key2]))
print(f'Дублируются: {common_set}')
for item in common_set:
    for name in items:
        if item not in items[name]:
            print(f'У {name} нет предмета {item}, а у минимум двоих есть')

