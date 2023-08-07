# Задача: Расчет финансовых показателей портфеля акций
# # Описание задачи:
# Вы являетесь инвестором и хотите создать программу для расчета нескольких финансовых показателей вашего портфеля
# акций.  Создайте модуль Python под названием "portfolio.py", который будет содержать функции для выполнения
# следующих операций:
#
# Расчет общей стоимости портфеля акций: Функция calculate_portfolio_value(stocks: dict, prices: dict) -> float
# принимает  два аргумента: stocks - словарь, где ключами являются символы акций (например, "AAPL" для Apple Inc.),
# и  значениями - количество акций каждого символа. prices - словарь, где ключами являются символы акций,
# а значениями  - текущая цена каждой акции. Функция должна вернуть общую стоимость портфеля акций на основе
# количества  акций и их текущих цен. Пример: Пришло
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
#
# Вышло:
# 16410,25
#
# Расчет доходности портфеля: Функция calculate_portfolio_return(initial_value: float, current_value: float) -> float
# принимает два аргумента: initial_value - начальная стоимость портфеля акций. current_value - текущая стоимость
# портфеля  акций. Функция должна вернуть процентную доходность портфеля. Пример:
# Пришло:
# 10000.0
# 15000.0
# Вышло:
# 50%
#
# Определение наиболее прибыльной акции: Функция get_most_profitable_stock(stocks: dict, prices: dict) -> str
# принимает  два аргумента: stocks - словарь с акциями и их количеством. prices - словарь с акциями и их текущими
# ценами.  Функция должна вернуть символ акции (ключ), которая имеет наибольшую прибыль по сравнению с ее начальной
# стоимостью. Начальная стоимость - первый вызов calculate_portfolio_value, данные из этого вызова следует сохранить
# в защищенную переменную на уровне модуля.
# Пример:
# Пришло:
# stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
# prices = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
# Вышло:
# MSFT

import copy


def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _counter
    global _INITIAL_PRISES
    if _counter == 0:
        _INITIAL_PRISES = copy.deepcopy(prices)
    cur_value = sum((prices[key] * stocks[key] for key in stocks))
    _counter += 1
    return cur_value


def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    diff = current_value - initial_value
    return diff / initial_value * 100


def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    # расчет по макс.процентам:
    # profit_list = {key: calculate_portfolio_return(_INITIAL_PRISES[key], prices[key]) for key in prices}

    # расчет по абсолютной доходности:
    profit_list = {key: (prices[key]) * stocks[key] - _INITIAL_PRISES[key] * stocks[key] for key in prices}

    most_prof_st = next(iter(profit_list))

    for key in profit_list:
        if profit_list[key] > profit_list[most_prof_st]:
            most_prof_st = key
    return most_prof_st


if __name__ == '__main__':
    _counter = 0
    _INITIAL_PRISES = {}
    stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
    prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}
    print('Portfolio value today is', calculate_portfolio_value(stocks, prices))
    print('Profit -', calculate_portfolio_return(1000, 1200), '%')

    cur_prises = {"AAPL": 155.25, "GOOGL": 2600.75, "MSFT": 800.50}
    print('Most profitable stock in portfolio -', get_most_profitable_stock(stocks, cur_prises))
