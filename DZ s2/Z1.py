# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input('Введите количество монет: '))
orel = 0
reshka = 0
for i in range(n):
    v = int(input('Введите сторону монеты(0/1: )'))
    if v == 1:
        orel += 1
    else:
        reshka +=1
if orel<reshka:
    print(orel)
else:
    print(reshka)