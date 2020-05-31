import numpy as np
from one_dimensional import fibonacci_method, unisearch_method


def func1(x):
    """x^2 + 2y^2 + sin(x+2y) + 3x + 2y"""
    return x[0] ** 2 + 2 * (x[1] ** 2) + np.sin(x[0] + 2 * x[1]) + 3 * x[0] + 2 * x[1]


def der_func1(x):
    return np.array([2 * x[0] + np.cos(x[0] + 2 * x[1]) + 3, 4 * x[1] + 2 * np.cos(x[0] + 2 * x[1]) + 2])


def func2(x):
    """(x^2 - y)^2 + (x-1)^2"""
    return (x[0] ** 2 - x[1]) ** 2 + (x[0] - 1) ** 2


def der_func2(x):
    return np.array([4 * x[0] * (x[0] ** 2 - x[1]) + 2 * (x[0] - 1),
                     -2 * (x[0] ** 2 - x[1])])


def steepest_gradient_descent(f, df, eps, x_0, step_method):
    x = x_0
    counter = 0
    while (lambda v: (v[0] ** 2 + v[1] ** 2) ** 0.5)(df(x)) >= eps:
        alpha = step_method(0, 1, lambda a: f(x - a * df(x)), eps)
        x -= alpha[0] * df(x)
        counter += 1
    print(counter)
    return x


xs = [-0.6799281866848323, 2.420223444760598, 4.388096788407111, 0]
ys = [-0.14010337286254337, -2.718572313201977, -2.4726769096483445, 0]

epsilon = 1e-6

res = steepest_gradient_descent(func1, der_func1, epsilon, [xs[2], ys[2]], fibonacci_method)
print(res)
