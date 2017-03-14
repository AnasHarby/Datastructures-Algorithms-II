from time import time
from random import randint


def _negate(args, start_ind, end_ind):
    for i in range(start_ind, end_ind):
        args[i] = - args[i]


def _reverse(args, start_ind, end_ind):
    rev = reversed(args[start_ind:end_ind])
    args[start_ind:end_ind] = rev


def _swap(args, start_ind, end_ind):
    for i in range(start_ind, end_ind - 1):
        args[i], args[i + 1] = args[i + 1], args[i]


def get_random_case(n, rng):
    """Generates a new random case with size n and range rng.

    :type n: int
    :param n: Size of the array"""
    x = []
    for i in range(n):
        x.append(randint(0, rng))
    return x


def get_sorted_reversed_case(n, rng):
    """Generates a new random reversed and sorted case with size n and range rng.

    :type n: int
    :param n: Size of the array"""
    return list(reversed(sorted(get_random_case(n, rng))))


def get_almost_sorted_case(n, rng):
    if n == 0:
        return []
    args = sorted(get_random_case(n, rng))
    functions = [_reverse, _negate, _swap]
    random_func = functions[randint(0, 2)]
    print(random_func)
    start_ind = randint(0, len(args) - 1)
    end_ind = randint(start_ind + 1, len(args))
    print(start_ind, end_ind)
    random_func(args, start_ind, end_ind)
    return args


def measure_algorithm(args, func):
    """"Measures time taken to execute a function.

    :type func: function
    :param func: Function to be measured."""
    start = time()
    func(args=args)
    end = time()
    return end - start
