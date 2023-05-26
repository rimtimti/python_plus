# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

import defs

class Bank:
    _BALANCE = 0
    _MIN_CASH = 50
    _MAX_CASH = 5_000_000
    _SUM_FOR_TAX = 5_000_000
    _COMMISSION = 0.015
    _MAX_COMMISSION = 600
    _MIN_COMMISSION = 30
    _BONUS = 0.03
    _TAX = 0.10
    _OPERATION: int

    def __init__(self):
        self._OPERATION = 0

    def _in(self, cash: int, tax: int) -> tuple[int, int]:
        self._BALANCE -= tax
        self._BALANCE += cash
        self._OPERATION += 1
        return self._BALANCE, self._OPERATION

    def _out(self, cash: int, commission: int, tax: int) -> tuple[int, int] | None:
        if self._BALANCE - (cash + commission + tax) >= 0:
            self._BALANCE -= cash + commission + tax
            self._OPERATION += 1
            return self._BALANCE, self._OPERATION
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        if sum_commission > self._MAX_COMMISSION:
            sum_commission = self._MAX_COMMISSION
        if sum_commission < self._MIN_COMMISSION:
            sum_commission = self._MIN_COMMISSION
        return int(sum_commission)

    def _check_tax(self, balance: int) -> int:
        if balance >= self._SUM_FOR_TAX:
            tax = round(balance * self._TAX)
            print(f'Внимание был снят {round(self._TAX * 100)} % налог на богатство в размере {tax}')
            return tax
        else:
            return 0

    def _exit(self):
        print('Всего доброго, приходите к нам еще')

    def _add_bonus(self):
            self._BALANCE += self._BALANCE * self._BONUS
            print(f'Поздравляем, вы получили бонус за каждую 3-ю операцию в нашем банке. На ваш счет было зачислено: {round(self._BALANCE * self._BONUS)}')

    def _menu(self, info: str, commands: str) -> str:
        '''
        Выводит на экран меню, возвращает выбранную команду
        '''
        choice = ''
        while choice not in commands:
            print(info)
            choice = input('Введите команду: ')
            if choice in commands:
                return choice
            else:
                print('Такой команды нет, попробуйте еще раз...')

    def start(self):
        '''
        Основная логика программы
        '''
        print('\nЭто программа "Банкомат".\nВы можете пополнять баланс и снимать со счета.\n')
        print('Сумма пополнения и снятия кратны 50 у.е.\n' \
        'Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.\n' \
        'После каждой третей операции пополнения или снятия начисляются проценты - 3%\n' \
        'При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной')
        while True:
            if self._OPERATION % 3 == 0 and self._OPERATION > 0:
                self._add_bonus()
            print(f'\nВаш баланс: {int(self._BALANCE)}')
            choice = self._menu('\nОСНОВНОЕ МЕНЮ:\n1 - пополнить баланс\n2 - снять средства\n3 - выход', ['1', '2', '3'])
            match choice:
                case '3':
                    print('Всего доброго, приходите к нам еще')
                    break
                case '1':
                    tax = self._check_tax(self._BALANCE)
                    cash = defs.get_natural_int_between_number('Введите сумму: ', self._MIN_CASH, self._MAX_CASH)
                    if cash % self._MIN_CASH != 0:
                        print(f'Введена сумма, которая не кратна 50')
                    self._in(cash=cash, tax=tax)
                    print(f'Средства были зачислены успешно сумма: {cash}, баланс: {int(self._BALANCE)}')
                case '2':
                    tax = self._check_tax(self._BALANCE)
                    cash = defs.get_natural_int_between_number('Введите сумму: ', self._MIN_CASH, self._MAX_CASH)
                    if cash % self._MIN_CASH != 0:
                        print(f'Введена сумма, которая не кратна 50')
                    commission = self._check_commission(cash=cash)
                    data = self._out(cash=cash, commission=commission, tax=tax)
                    if data:
                        print(f'Средства были сняты успешно, сумма: {cash}, коммисия: {commission}, баланс: {int(self._BALANCE)}')
                    else:
                        print('У Вас недостаточно средств для проведения данной операции')

bank = Bank()
bank.start()
