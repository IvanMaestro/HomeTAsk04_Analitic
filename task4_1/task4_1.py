# Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$


from decimal import Decimal


def rounding(num, accuracy):
    n = Decimal(f'{num}')
    return n.quantize(Decimal(f'{accuracy}'))


number = float(input('Введите вещественное число: '))
d = float(input('Введите точность округления (например: 0.0001): '))

print(rounding(number, d))
