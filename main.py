# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения
# n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# m = int(input('Введите размер списка: '))
# a1 = int(input('Введите значение первого элемента: '))
# d = int(input('Введите значение разности: '))
#
# list_1 = []
# for i in range(m):
#     m1 = a1 + d * i
#     list_1.append(m1)
# print(list_1)


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

m = int(input('Введите размер списка: '))
list_1 = []
for i in range(m):
    i = random.randint(0, 100)
    list_1.append(i)
print(list_1)

max_ind = 0
min_ind = 0
max_count = 0
min_count = 100
for i in range(len(list_1)):
    if list_1[i] > max_count:
        max_count = list_1[i]
        max_ind = i + 1
    if list_1[i] < min_count:
        min_count = list_1[i]
        min_ind = i + 1
print(f'индекс с максимальным значением: {max_ind} и с минимальным: {min_ind}')

if max_ind > min_ind:
    for i in range(len(list_1)):
        if max_ind >= i >= min_ind:
            print(i)
else:
    for i in range(len(list_1)):
        if max_ind <= i <= min_ind:
            print(i)
