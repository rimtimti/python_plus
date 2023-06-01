# Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# целое положительное число
# вещественное положительное или отрицательное число
# строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# строку в верхнем регистре в остальных случаях

def task_2():
    input_user = input("Введите данные: ")
    if input_user.isdigit():
        print('Это целое положительное число.')
        result = int(input_user)
    elif (input_user.count(".") == 1 or (input_user.count("-") == 1 and input_user.startswith("-"))) \
            and (input_user.replace("-", "").replace(".", "").isdigit()):
        result = float(input_user)
        print('Это вещественное положительное или отрицательное число.')
    elif not input_user.islower():
        result = input_user.lower()
        print('Это строка, где есть хотя бы одна заглавная буква.')
    else:
        result = input_user.upper()
        print('Это другая строка.')
    print(f"{result}")


task_2()
