import numpy as np
from tabulate import tabulate
import math


def fourth(x):
    """a=-3, b=3"""
    return x ** 3 - x + math.exp(-x)


def fifth(x):
    """a=0, b=1"""
    return x ** 4 + math.exp(-x)


def test_f(x):
    """a=-3, b=5"""
    return x * x + 2 * x


def fibonacci(f_n):
    a, b = 1, 1
    while a < f_n:
        yield a
        a, b = b, a + b
    yield a


def fibonacci_method(a, b, f, eps):
    F = list(fibonacci(np.ceil((b - a) / eps)))
    n, k = len(F) - 1, 0
    func_call_counter = 1
    data = []
    c = a + (b - a) * F[n - k - 2] / F[n - k]
    d = a + (b - a) * F[n - k - 1] / F[n - k]
    f_c, f_d = f(c), f(d)
    while k < n - 1:
        data.append((a, b, b - a, c, d, f_c, f_d))
        if f_c > f_d:
            a, c = c, d
            d = a + (b - a) * F[n - k - 2] / F[n - k - 1]
            f_c, f_d = f_d, f(d)
        else:
            b, d = d, c
            c = a + (b - a) * F[n - k - 3] / F[n - k - 1]
            f_d, f_c = f_c, f(c)
        k += 1
        func_call_counter += 1
    data.append((a, b, b - a, None, None, None, None))
    return [(a + b) / 2, f((a + b) / 2), func_call_counter, data]


# columns = ['a', 'b', 'interval', 'x1', 'x2', "f(x1)", "f(x2)"]
# left, right = -3, 5
# epsilon = 0.2
#
# print("Метод ФИБОНАЧИ: eps = {}".format(epsilon))
# res = fibonacci_method(left, right, test_f, epsilon)
# # print(tabulate(res[3], headers=columns, floatfmt=".6f", tablefmt='github', showindex="always"))
# print("Результат:\t   x = {:.6f}\tf(x) = {:.6f}\nЧисло вызовов функции: {}\n".format(res[0], res[1], res[2]))


def unisearch_method(a, b, f, eps, base_n=10):
    x_opt = a
    separation_counter = 0
    while b - a >= 2 * eps:
        xs = [a + i * (b - a) / base_n for i in range(base_n + 1)]
        fs = [f(x) for x in xs]
        arg_min_f = int(np.argmin(fs))
        x_opt = xs[arg_min_f]
        separation_counter += 1
        if 0 < arg_min_f < base_n:
            a, b = xs[arg_min_f - 1], xs[arg_min_f + 1]
        elif arg_min_f == 0:
            a, b = xs[arg_min_f], xs[arg_min_f + 2]
        else:
            a, b = xs[arg_min_f - 2], xs[arg_min_f]
    return [x_opt, f(x_opt), b - a]


# print("Метод РАВНОМЕРНОГО ПОИСКА: eps = {}".format(epsilon))
# res = unisearch_method(left, right, test_f, epsilon)
# print("Результат:\t   x = {:.6f}\tf(x) = {:.6f}\nКонечный интервал: {}\n".format(res[0], res[1], res[2]))
