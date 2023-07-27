# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции. Дополнительно сохраняйте все
# операции поступления и снятия средств в список.
account = 0
history = []
op_counter = 0


def addition(amount: float) -> account:
    global account
    global op_counter
    if amount % 50 == 0 and amount >= 50:
        account += amount
        history.append(('added', amount))
        op_counter += 1
        if op_counter % 3 == 0:
            account *= 1.03
            history.append(("Bonus for each third operation. 3% has been added to account", amount))
    else:
        print('Sum should be div.50/ Operation denied')
        history.append('Operation denied')
        return


def withdrawal(amount: float):
    global account
    global op_counter
    if amount % 50 == 0 and amount <= account:
        account -= amount
        history.append(('withdraw', amount))
        op_counter += 1
        if op_counter % 3 == 0:
            account *= 1.03
            history.append(("Bonus for each third operation. 3% has been added to account", amount))
    else:
        print('Sum should be div.50 or sum > account/ Operation denied')
        return


def check_sum():
    print(f'Your {account = :.2f}')


addition(100)
addition(75)
addition(150)
withdrawal(34)
withdrawal(200)
check_sum()
print(history)
