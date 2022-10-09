# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import numpy
from random import randrange


# 1 Вариант

def rand_num(count: int):
    if count < 0:
        print('Не может быть такого количества элементов')
        return []

    some_list = []
    for i in range(count):
        some_list.append(randrange(count))

    return some_list


def find_elem(some_list: list):
    res = []
    new_dict = {}.fromkeys(some_list, 0)

    for i in some_list:
        new_dict[i] += 1

    for j in new_dict:
        if new_dict[j] == 1:
            res.append(j)

    return res


n = int(input('Введите количество чисел: '))

new_list = rand_num(n)
print(f'Список неповторяющихся элементов последовательности {new_list}:\n{find_elem(new_list)}')

# 2 Вариант

# def find_non_repeat(some_list):
#     new_list = []
#     for i in some_list:
#         if some_list.count(i) > 1:
#             continue
#         else:
#             new_list.append(i)
#     return new_list
#
#
# items = numpy.random.randint(10, size=10)
# input_list = list(items[:10])
# print(f'Список неповторяющихся элементов последовательности {input_list}:\n{find_non_repeat(input_list)}')

# ===========================================================================================================
# Дальше не мои решения
# 3 Вариант

# dict_new = {}
# items = numpy.random.randint(10, size=10)
# input_list = list(items[:10])
# for i in input_list:
#     if not i in dict_new:
#         dict_new[i] = 0
#     dict_new[i] += 1
#
# res_list = []
# for i in dict_new:
#     if dict_new[i] == 1:
#         res_list.append(i)
# print(input_list)
# print(res_list)

# ============================================================================================================

# from collections import Counter
#
# dict_new = {}
# items = numpy.random.randint(10, size=10)
# input_list = list(items[:10])
#
# dict_new = Counter(input_list)
# res_list = [i for i in dict_new if dict_new[i] == 1]
#
# print(input_list)
# print(res_list)
