# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

# n = int(input('Введите количество монет: '))
# orel = 0
# reshka = 0
# for i in range(n):
#     v = int(input('Введите сторону монеты(0/1: )'))
#     if v == 1:
#         orel += 1
#     else:
#         reshka +=1
# if orel < reshka:
#     print(orel)
# else:
#     print(reshka)

# --------------------------------------------------------

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# x = int(input('Введите сумму 2х чисел от 0 до 1000: '))
# y = int(input('Введите произведение 2х чисел от 0 до 1000: '))
# if x < 1 or x > 1000 or y < 1 or y > 1000:
#     print('Вы ввели число не из заданного диапазона!')
# else:
#     d1 = int((x + ((-x) ** 2 - 4 * y) ** 0.5) / 2)
#     d2 = int((x - ((-x) ** 2 - 4 * y) ** 0.5) / 2)
#     print(d1, d2)

# --------------------------------------------------------

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


n = int(input('Введите число: '))
i = 0
while 2 ** i <= n:
    print(2 ** i,end=" ")
    i += 1