# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randint
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
import defs

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
COUNTER = 10

number = randint(LOWER_LIMIT, UPPER_LIMIT)
print(
    f"Попробуйте угадать число от {LOWER_LIMIT} до {UPPER_LIMIT}, которое загадал компьютер."
)
while COUNTER != 0:
    print(f"У вас осталось {COUNTER} попыток.")
    user_number = defs.get_natural_int_between_number(
        f"Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: ", LOWER_LIMIT, UPPER_LIMIT
    )
    if user_number < number:
        print("Вы ввели число меньше загаданного.")
    elif user_number > number:
        print("Вы ввели число больше загаданного.")
    else:
        print(f"Вы угадали, это число {number}.")
        break
    COUNTER -= 1
    if COUNTER == 0:
        print(f"К сожалению, ваши попытки закончились, это было число {number}.")
