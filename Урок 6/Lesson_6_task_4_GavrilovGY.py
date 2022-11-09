# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from random import uniform
import math

n = int(input('Введите размер списка: '))
list_1 = [round(uniform(0,9),2) for i in range(n)]
list_2 = []
for i in range(len(list_1)):
    j = list_1[i] - math.trunc(list_1[i])
    list_2.append(round(j, 2))

min = min(list_2, key = lambda i: float(i))
max = max(list_2, key = lambda i: float(i))

dif = (max - int(max)) - (min - int(min))

print(f'Список из случайных чисел размерности "{n}": {list_1}')
print(f'Максимальная дробная часть: {max}, \nМинимальная дробная часть: {min}')
print(f'Разница между максимальным и минимальным значениями дробных частей: {round(dif,2)}')