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
    _MAX_CASH = 10_000_000
    _SUM_FOR_TAX = 5_000_000
    _COMMISSION = 0.015
    _MAX_COMMISSION = 600
    _MIN_COMMISSION = 30
    _BONUS = 0.03
    _TAX = 0.10
    _BONUS_OPERATION = 3
    _COUNTER: int
    _HISTORY: list[str]

    def __init__(self):
        self._COUNTER = 0
        self._HISTORY = []

    def _in(self, cash: int) -> tuple[int, int]:
        self._BALANCE += cash
        return self._BALANCE

    def _out(self, cash: int, commission: int) -> tuple[int, int] | None:
        if self._BALANCE - (cash + commission) >= 0:
            self._BALANCE -= cash + commission
            return self._BALANCE
        else:
            return None

    def _check_commission(self, cash: int) -> int:
        sum_commission = cash * self._COMMISSION
        if sum_commission > self._MAX_COMMISSION:
            sum_commission = self._MAX_COMMISSION
        if sum_commission < self._MIN_COMMISSION:
            sum_commission = self._MIN_COMMISSION
        return int(sum_commission)

    def _check_operation(self):
        self._COUNTER += 1
        cash = defs.get_natural_int_between_number(f'Введите сумму от {self._MIN_CASH:_} до {self._MAX_CASH:_}: ', self._MIN_CASH, self._MAX_CASH)
        if cash % self._MIN_CASH != 0:
            print(f'Введена сумма, которая не кратна {self._MIN_CASH:_}')
            return self._check_operation()
        return cash

    def _check_tax(self) -> int:
        if self._BALANCE >= self._SUM_FOR_TAX:
            tax = int(round(self._BALANCE * self._TAX))
            self._BALANCE -= tax
            text = f'Внимание был снят {round(self._TAX * 100)} % налог на богатство в размере {tax:_}, баланс: {self._BALANCE:_}'
            self._HISTORY.append(text)
            print(text)


    def _exit(self):
        print('\nВсего доброго, приходите к нам еще')

    def _add_bonus(self) -> None:
        if self._COUNTER % self._BONUS_OPERATION == 0 and self._COUNTER > 0:
            bonus = int(round(self._BALANCE * self._BONUS))
            self._BALANCE += bonus
            text = f'Поздравляем, вы получили бонус за каждую 3-ю операцию в нашем банке. На ваш счет было зачислено: {bonus:_}, баланс: {self._BALANCE:_}'
            self._HISTORY.append(text)
            print(text)

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

    def _show_history(self) -> None:
        for i in self._HISTORY:
            print(i)

    def start(self):
        '''
        Основная логика программы
        '''
        print('\nЭто программа "Банкомат".\nВы можете пополнять баланс и снимать со счета.\n')
        print(f'Сумма пополнения и снятия кратны {self._MIN_CASH:_} у.е.\n' \
        f'Маскимально можно положить на счет {self._MAX_CASH} у.е.\n' \
        f'Процент за снятие — {self._COMMISSION * 100}% от суммы снятия, но не менее {self._MIN_COMMISSION:_} и не более {self._MAX_COMMISSION:_} у.е.\n' \
        f'После каждой {self._BONUS_OPERATION} операции пополнения или снятия начисляются проценты - {self._BONUS * 100}%\n' \
        f'При превышении суммы в {self._SUM_FOR_TAX:_}, вычитается налог на богатство {self._TAX * 100}% перед каждой операцией, даже ошибочной')
        while True:
            print(f'\nВаш баланс: {self._BALANCE:_}')
            choice = self._menu('\nОСНОВНОЕ МЕНЮ:\n1 - пополнить баланс\n2 - снять средства\n3 - показать историю операций\n4 - выход', ['1', '2', '3', '4'])
            match choice:
                case '4':
                    self._exit()
                    break
                case '3':
                    self._show_history()
                case '1':
                    self._check_tax()
                    cash = self._check_operation()
                    self._in(cash=cash)
                    text = f'Средства были зачислены успешно сумма: {cash:_}, баланс: {self._BALANCE:_}'
                    self._HISTORY.append(text)
                    print(text)
                    self._add_bonus()
                case '2':
                    self._check_tax()
                    cash = self._check_operation()                    
                    commission = self._check_commission(cash=cash)
                    data = self._out(cash=cash, commission=commission)
                    if data:
                        text = f'Средства были сняты успешно, сумма: {cash:_}, коммисия: {commission:_}, баланс: {self._BALANCE:_}'
                        self._HISTORY.append(text)
                        print(text)
                        self._add_bonus()
                    else:
                        print('У Вас недостаточно средств для проведения данной операции')

bank = Bank()
bank.start()
