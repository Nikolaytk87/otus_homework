"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    """
    return [num ** 2 for num in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_of_nums, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)
    """
    result_numbers = []
    if filter_type == 'odd':
        result_numbers = [num for num in list_of_nums if num % 2 != 0]
    elif filter_type == 'even':
        result_numbers = [num for num in list_of_nums if num % 2 == 0]
    elif filter_type == 'prime':
        result_numbers = [num for num in list_of_nums if is_prime(num) and num > 1]
    return result_numbers


def is_prime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    result = filter_numbers([1, 4, 6, 8, 946, 3, 2, 13, 14, 19, 25], 'odd')
    print(result)
