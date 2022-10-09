# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

import math


# 2 Вариант более красивый

def search_common_mult(num):
    div = 2
    some_list = []
    while num > 1:
        if num % div == 0:
            some_list.append(div)
            num /= div
        else:
            div += 1
    return some_list


n = int(input('Введите натуральное число: '))

print(f'Список простых множителе числа {n}:\n{search_common_mult(n)}')

# 1 Вариант. Вложеные циклы

# def find_common_mult(num):
#     some_list = []
#     while num % 2 == 0:
#         some_list.append(2)
#         num = num / 2
#
#         for i in range(3, int(math.sqrt(num))+ 1,2):
#             while(num % i == 0):
#                 some_list.append(i)
#                 num /= i
#         if num >1:
#             some_list.append(int(num))
#         return some_list
#
# n = int(input('Введите натуральное число: '))
#
# print(f'Список простых множителе числа {n}:\n{find_common_mult(n)}')
