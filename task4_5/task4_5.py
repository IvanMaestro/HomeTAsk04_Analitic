# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from random import choice


def poly(str_1: str, str_2: str):
    with open(str_1, 'r', encoding='utf-8') as my_file_1, \
            open(str_2, 'r', encoding='utf-8') as my_file_2:
        first = my_file_1.readlines()
        second = my_file_2.readlines()

        if len(first) == len(second):
            with open('poly_summ.txt', 'a', encoding='utf-8') as my_file_3:
                for i, v in enumerate(first):
                    my_file_3.write(f'{v[:-5]} + {second[i]}')
        else:
            print('Данные файлов не совпадают')


poly('poly.txt', 'poly_2.txt')
