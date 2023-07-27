# Напишите функцию принимающую, на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного  аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

def revert(**kwargs) -> dict:
    rev_dict = {}

    for key, value in kwargs.items():
        if type(value) == list or set or dict:
            value = str(value)
        rev_dict[value] = key
    return rev_dict


print(revert(a=12, b='укроп', c=[12, 'num'], d=22, f1=(12, 'рыба')))
