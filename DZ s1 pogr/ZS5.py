# Z1
# Напишите функцию f, которая на вход принимает два числа a и b, и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.
# Пример:
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 


a = int(input("Введите число: "))
b = int(input("Введите степень числа: "))


def func(a, b):
    if b == 0:
        return 1

    return a * func(a, b - 1)


print(func(a, b))

# ----------------------------------------------------------

#Z2
#  Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# Пример:
# sum(2, 2)
# 4

# a = int(input("Введите 1е число: "))
# b = int(input("Введите 2е число: "))

# def sum(a, b):
#     if a == 0:
#         return b
#     return sum(a - 1, b + 1)

# print(sum(a, b))