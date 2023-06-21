# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.

list_1 = [5, 2, 4, 1]
k = 1
# find_num = 0

# index_element = 0
# min_element = abs(k - list_1[0])
# for i in range(1, len(list_1)):
#     buffer_element = abs(k -list_1[i])
#     if buffer_element < min_element:
#         min_element = buffer_element
#         index_element = i
# print([index_element])

max = list_1[0]
for i in range(len(list_1)):
    if abs(list_1[i] - k) < abs(max - k):
        max = list_1[i]
print(max)