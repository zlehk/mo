import numpy as np
from mo_gradient.funcs import func, der_func, der_der_func, norm2
from tabulate import tabulate


def first_order(f, df, x_0, eps, alpha):
    """Градиентный метод 2-го порядка"""
    x = x_0
    iterations = 0
    x_next = x - alpha * df(x)
    while norm2(df(x)) >= eps:
        x, x_next = x_next, x - alpha * df(x)
        iterations += 1
    return [x, iterations]


# xs = [-5.785685835824241, -4.322697383792522, -2.240651381500233, -2.1931138685586804, -0.6799281866848323,
#       0.6442180763909864, 2.302006495708799, 2.420223444760598, 4.388096788407111, 6.1256254032859285]
# ys = [2.5591253949120842, 1.57416568843803, 0.5502991528690719, -0.46431826282763566, -0.14010337286254337,
#       -1.012376059460888, -1.3241578701223444, -2.718572313201977, -2.4726769096483445, -3.662889903151375]

xs = [-0.6799281866848323, 2.420223444760598, 4.388096788407111]
ys = [-0.14010337286254337, -2.718572313201977, -2.4726769096483445]

x_opt = np.array([-1.31593273, -0.31593273])
columns = ['x_0', 'y_0', 'шаги', 'x_opt', 'y_opt', 'оценка погрешности', 'фактическая погрешность']

r = np.linalg.norm(der_der_func([-np.pi / 2, 0]), ord=2)
o_eps = 0.1
o_alpha = (1 - o_eps) / r

points = []
print()
for k in range(len(xs)):
    i = xs[k]
    j = ys[k]
    o_x_0 = np.array([i, j])
    res = first_order(func, der_func, o_x_0, o_eps, o_alpha)

    points.append([i, j, res[1], res[0][0], res[0][1], norm2(der_func(res[0])) / 2, norm2(res[0] - x_opt)])

print('eps: {}'.format(o_eps))
print(tabulate(points, headers=columns, floatfmt=".4f", tablefmt='github', showindex="always"))

o_eps = 0.01

points = []
print()
for k in range(len(xs)):
    i = xs[k]
    j = ys[k]
    o_x_0 = np.array([i, j])
    res = first_order(func, der_func, o_x_0, o_eps, o_alpha)

    points.append([i, j, res[1], res[0][0], res[0][1], norm2(der_func(res[0])) / 2, norm2(res[0] - x_opt)])

print('eps: {}'.format(o_eps))
print(tabulate(points, headers=columns, floatfmt=".4f", tablefmt='github', showindex="always"))
