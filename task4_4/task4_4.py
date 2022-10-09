# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import choice


def polynomial(num: int):
    if num < 1:
        return 0

    polynom = ''
    some_list = range(0, 100)

    with open('polynomial.txt', 'a', encoding='utf-8') as my_file:
        for i in range(num, 0, -1):
            val = choice(some_list)
            if val:
                polynom += f'{val}*x^{i} {choice("+-")} '

        my_file.write(f'{polynom}{choice(some_list)} = 0\n')


k = int(input('Введите степень К: '))
polynomial(k)
