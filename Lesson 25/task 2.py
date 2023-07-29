# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: имена str,
# ставка int,  премия str с указанием процентов вида «10.25%». В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка умноженная на процент премии

name_list = ['Ivan', 'Petr', 'Silver', 'Trelony']
stake_list = [200, 250, 300, 100]
bonus_list = ['-5%', '10.2%', '7%', '12.76%']
salary_list = {name: stake_list[name_list.index(name)] * float(bonus_list[name_list.index(name)][:-1]) / 100
               for name in name_list}
print('Bonus/fine:', *salary_list.items())
