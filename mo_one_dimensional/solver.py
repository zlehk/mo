import math
from mo_one_dimensional.dichotomy import dichotomy_method
from mo_one_dimensional.golden_ratio import golden_ration_method
from tabulate import tabulate


def first(x):
    # a, b = 1.5, 3.5
    return math.sin(2 * x) * math.log(x)


def second(x):
    # не трудно прикинуть
    return x ** 2


def third(x):
    # a, b = 2, 3.5
    return math.sin(x) * ((math.cos(x)) ** 3)


def fourth(x):
    # не помню
    return x ** 3 - x + math.exp(-x)


def fifth(x):
    # a, b = -3, 3
    return x ** 4 + math.exp(-x)


a, b = -3, 3
eps = 1e-4

golden_columns = ['a', 'b', 'interval', 'x1', 'x2', "f(x1)", "f(x2)"]
print("Метод ЗОЛОТОГО СЕЧЕНИЯ: eps = {}".format(eps))
res = golden_ration_method(a, b, eps, fifth)
print(tabulate(res[3], headers=golden_columns, floatfmt=".6f", tablefmt='github', showindex="always"))
print("Результат:\t   x = {:.6f}\tf(x) = {:.6f}\nЧисло вызовов функции: {}".format(res[0], res[1], res[2]))

dichotomy_columns = ['a', "b", "x1", "x2", "f(x1)", "f(x2)", "b-a"]

print("Метод ДИХОТОМИИ: eps = {}".format(eps))
res = dichotomy_method(a, b, eps, fifth)
print(tabulate(res[3], headers=dichotomy_columns, floatfmt=".8f", tablefmt='github', showindex="always"))
print("Результат:\n   x = {:.10f}\nf(x) = {:.10f}\nЧисло вызовов функции: {}".format(res[0], res[1], res[2]))
