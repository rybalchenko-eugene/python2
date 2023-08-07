import random
from random import randint

def chess_check(chess_set: list) -> bool:
    lines = len(chess_set)
    for line in chess_set[1:]:
        for previous in chess_set[:chess_set.index(line)]:
                if line[1] == previous[1] or line[0] - previous[0] == abs(line[1] - previous[1]) and chess_set:
                    return False
    return True

def set_chess(lines = 8, scheme_amount = 4):

    # lines = 8       размер доски
    # number_sc = 4   нужное кол-во вариантов расстановки

    counter = 1
    while scheme_amount > 0:
        history = []
        ost_row = [x for x in range(1, lines + 1)]
        scheme = True
        for line in range(1, lines + 1):
            var_line = ost_row.copy()

            while len(var_line) != 0:
                find = True
                attemp = var_line[randint(0, len(var_line)) - 1]

                for step in history:
                    if line - step[0] == abs(step[1] - attemp):
                        if attemp in var_line:
                            var_line.remove(attemp)
                            find = False
                        else:
                            find = False
                            break
                if find:
                    ost_row.remove(attemp)
                    history.append((line, attemp))
                    break
            if not find:
                scheme = False
                break

        counter += 1
        if scheme:
            scheme_amount -= 1
            print(f'{counter = }')
            print(history)

if __name__ == '__main__':
    set_chess()
    print(chess_check([(1, 7), (2, 3), (3, 1), (4, 6), (5, 8), (6, 5), (7, 2), (8, 4)]))