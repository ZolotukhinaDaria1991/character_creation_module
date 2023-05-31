from math import sqrt

message = 'Добро пожаловать в самую лучшую программу для вычисления '
'квадратного корня из заданного числа'


def CalculateSquareRoot(Number):
    '''Вычисляет квадратный корень'''
    return sqrt(Number)


def calc(your_number):
    root = 0
    if your_number <= 0:
        root = 0
    else:
        root = CalculateSquareRoot(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {root}')


print(message)
calc(25.5)


def main():
    print(print.__doc__)


main()
