# 1) Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

x = [2, 5, 9, 12, 17, 20, 3]

summ = 0
for i in range(1, len(x), 2):
    summ += x[i]       
print(f"{x} -> сумма элементов на нечётных позициях: {summ}")

# 2) Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

from random import randint


number = int(input('Введите размер списка '))
list = []
list2 = []

for i in range(number):
    list.append(randint(0, 9))

for i in range(len(list)):
    while i < len(list)/2 and number > len(list)/2:
        number = number - 1
        a = list[i] * list[number]
        list2.append(a)
        i += 1

print(list)
print(list2)

# 3) Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

from random import uniform


n = int(input('Введите размер списка '))
list1 = []
for i in range(n):
    f = uniform(0, 9)
    list1.append(round(f, 2))

min = list1[0]
max = 0
for i in range(len(list1)):
    
    if max < list1[i]:
        max = list1[i]
    if min > list1[i]:
        min = list1[i]
dif = (max - int(max)) - (min - int(min))

print(list1)
print(f'max: {max}, min: {min}')
print(round(dif,2))

# 4) Напишите программу, которая будет преобразовывать десятичное число в двоичное.

a = int(input('Введите число в десятичной системе исчисления: '))
b = ''
while a > 0:
    b = str(a%2) + b
    a = a // 2
print(f'Число в двоичной системе исчисления: {b}')

