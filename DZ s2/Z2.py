# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

x = int(input('Введите сумму 2х чисел от 0 до 1000: '))
y = int(input('Введите произведение 2х чисел от 0 до 1000: '))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    d1 = int((x + ((-x) ** 2 - 4 * y) ** 0.5) / 2)
    d2 = int((x - ((-x) ** 2 - 4 * y) ** 0.5) / 2)
    print(d1, d2)