# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15


a = int(input("Введите первый элемент: "))
b = int(input("Введите шаг: "))
n = int(input("Введите количество элементов: "))

list1 = []
for i in range(n):
# while n > 0:
    an = a + i * b
    # n -= 1
    list1.append(an)
# list1.reverse()
print(list1)

