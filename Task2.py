# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

from functools import reduce
import math


# факториал для примера

print(reduce(lambda x, y: x * y, range(1, (int(input('Введите целое число N => ')))+1), 1))

# варианты

print(list(map(lambda x: ((x == 1) and 1) or x * math.factorial(x - 1), list(range(1, (int(input('Введите целое число N => ')))+1)))))
print(list(map(lambda x: ((x == 1) and 1) or x * math.factorial(x - 1), range(1, (int(input('Введите целое число N => ')))+1))))
print(list(map(lambda x: math.factorial(x), range(1, (int(input('Введите целое число N => ')))+1))))



# вариант (для сравнения)
n = int(input('Введите целое число N => '))
f = 1
for i in range(n):
    i = i + 1
    f = i * f   
    print(f, end=" ")
