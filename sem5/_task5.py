# Напишите программу, которая выводит на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

START = 1
FINISH = 100
FIZZ = 3
BUZZ = 5


def fizz_buzz() -> None:
    print(
        *(
            "FizzBuzz"
            if i % (FIZZ * BUZZ) == 0
            else "Fizz"
            if i % FIZZ == 0
            else "Buzz"
            if i % BUZZ == 0
            else i
            for i in range(START, FINISH + 1)
        )
    )


fizz_buzz()
