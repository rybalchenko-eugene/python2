# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно
# быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

data = [54, 1, 2, 3, 1, 2, 4, 5, 54, 34, 1, 45, 78, 43, 33, 3, 54]
repeated_data = []
for example in data:
    count = 0
    for check in data:
        if example == check and example not in repeated_data:
            count += 1
            if count > 1:
                repeated_data.append(check)
                break
print(data)
print(repeated_data)
