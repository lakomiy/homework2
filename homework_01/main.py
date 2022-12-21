"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    ls = [x * x for x in args ]
    return ls


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
        k = 0
        for n in range(1, number + 1):
            if number % n == 0:
                k += 1
        if k == 2:
            return number


def filter_numbers(ls, args):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if args == ODD:
        return [x for x in ls if x % 2 != 0]
    elif args == EVEN:
        return [x for x in ls if x % 2 == 0]

    elif args == PRIME:
        ls_prime = list(filter(is_prime, ls))
        return ls_prime

