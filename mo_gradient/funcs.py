import numpy as np


def func(x, a=2, b=1, c=2):
    return x[0] ** 2 + a * (x[1] ** 2) + np.sin(b * x[0] + c * x[1]) + 3 * x[0] + 2 * x[1]


def der_func(x, a=2, b=1, c=2):
    return np.array(
        [2 * x[0] + b * np.cos(b * x[0] + c * x[1]) + 3, a * 2 * x[1] + c * np.cos(b * x[0] + c * x[1]) + 2])


def der_der_func(x, a=2, b=1, c=2):
    return np.array([[2 - b * b * np.sin(b * x[0] + c * x[1]), -b * c * np.sin(b * x[0] + c * x[1])],
                     [-b * c * np.sin(b * x[0] + c * x[1]), a * 2 - c * c * np.sin(b * x[0] + c * x[1])]])


def norm2(x):
    return (x[0] ** 2 + x[1] ** 2) ** 0.5
