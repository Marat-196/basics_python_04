# 3. Возьмите задачу о банкомате из семинара 2.
# Напишите программу банкомат.
# Начальная сумма равно нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е
# Процент за снятие - 1,5 % от суммы снятия, но не менее 30 и е более 600 у.е.
# После каждой третьей операции пополнения или снятия начисляются проценты - 3 %
# Нельзя снять больше, чем на счете
# При превышении суммы в 5 млн. вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег
import decimal

CMD_DEPOSIT = 'p'
CMD_WITHDRAW = 's'
CMD_EXIT = 'v'
RICHNESS_SUM = decimal.Decimal(5_000_000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(1000)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

sm_money = decimal.Decimal(0)
count = 0
wdt = 1


def withdraw_money(money):
    global sm_money, count, wdt
    wdt = money * WITHDRAW_PERCENT
    wdt = MIN_REMOVAL if wdt < MIN_REMOVAL else MAX_REMOVAL if wdt > MAX_REMOVAL else wdt
    if sm_money >= amount + wdt:
        sm_money -= money
        count += 1
        return sm_money
    return False


def add_money(money):
    global sm_money, count
    sm_money += money
    count += 1
    return sm_money


def richness_sm(val):
    percent = val * RICHNESS_TAX
    val -= percent
    return val


def val_dep_withdr(val):
    val = 1
    while val % 50 != 0:
        val = int(input(f"Введите сумму кратную {MULTIPLICITY} y.e.: "))
    return val


def cnt_oper(val):
    bonus_percent = val * ADD_PERCENT
    val += bonus_percent
    return val

while True:

    command = input(
        'Добрый день!\nДля пополнения счета введите клавишу - "p", \nдля снятия наличных введите клавишу - "s",\nдля выхода введите клавишу - "v": ')
    if command == CMD_EXIT:
        print("Операция завершена! Хорошего вам дня!")
        exit()
    if sm_money > RICHNESS_SUM:
        sm_money = richness_sm(sm_money)
        print(
            f'Удержан налог на богатство в размере {RICHNESS_TAX}%\nИтого на карте: {sm_money} y.e')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        ammount = val_dep_withdr(amount)
    if command == CMD_DEPOSIT:
        sm_money = add_money(ammount)
        print(f"Пополнение карты на {ammount} y.e\nИтого на карте {sm_money} y.e.")
    if command == CMD_WITHDRAW:
        if withdraw_money(ammount):
            print(f"Снятие с карты {ammount} y.e.\nКомиссия за снятие {wdt} y.e.\n"
                  f"На карте осталось {sm_money} y.e.")
        else:
            print(f"Недостаточно средств!\nНа карте {sm_money} y.e.")
    if count % COUNT_OPER == 0:
        sm_money = cnt_oper(sm_money)
        print(f"На ваш счет зачислено {ADD_PERCENT}%\nИтого на карте: {sm_money} y.e.")
