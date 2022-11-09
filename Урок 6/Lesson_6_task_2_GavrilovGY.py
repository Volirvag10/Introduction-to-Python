# 5. Реализуйте алгоритм перемешивания списка.

from random import Random, randint

N = int(input('Введите число: '))
numbers = [randint(-N,N) for i in range(N)]
print(f'Список случайных числе в пределах от {-N} до {N}:\n{numbers}')

def smes(numbers):
    list = numbers[:]
    numbers_length = len(list)
    for i in range(numbers_length):
        index = randint(0, numbers_length - 1)
        temp = list[i]
        list[i] = list[index]
        list[index] = temp
    return list
print(f'Перемешанный список случайных числе в пределах от {-N} до {N}:\n{smes(numbers)}')