# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1

list_1 = [3, 3, 3, 4, 5]
k = 3

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
       count += 1
print(count)


