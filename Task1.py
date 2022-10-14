# 1.Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

from functools import reduce

# вариант 1
n = [10, 20, 30, 40, 50, 60, 70, 80, 90]
sum = 0
print(list(enumerate(n)))

for index, value in enumerate(n):
    if index % 2:
        print(index, n[index])
        sum = sum + n[index]
print(sum)

# вариант 2
sum1 = reduce(lambda acc, elem: acc + (elem[1] if elem[0] % 2 else 0), enumerate(n), 0)
print(sum1)

# вариант 3
sum1 = reduce(lambda acc, elem: acc + n[elem], filter(lambda x: x % 2, range(len(n))), 0)
print(sum1)
