import numpy as np
from mo_gradient.funcs import func, der_func, der_der_func, norm2
import math
from tabulate import tabulate


def second_order(f, df, ddf, x_0, eps, e=0.47):
    """Градиентный метод 2-го порядка"""
    x = x_0
    iterations = 0
    while norm2(df(x)) ** 2 >= eps:
        iterations += 1
        alpha = 1
        p = -1 * np.dot(np.linalg.inv(ddf(x)), df(x))
        x_next = x + alpha * p
        chao = 0  # контролирует, не ушли ли в бесконечный цикл
        while f(x_next) - f(x) > e * alpha * np.dot(df(x), p) and chao < 10:
            chao += 1
            alpha /= 2
            x_next = x + alpha * p
        if chao == 10:  # ушли в бесконечный цикл
            x = [-100, -100]
            iterations = -100
            break
        else:
            x = x_next
    return [x, iterations]


xs = [-5.785685835824241, -4.322697383792522, -2.240651381500233, -2.1931138685586804, -0.6799281866848323,
      0.6442180763909864, 2.302006495708799, 2.420223444760598, 4.388096788407111, 6.1256254032859285]
ys = [2.5591253949120842, 1.57416568843803, 0.5502991528690719, -0.46431826282763566, -0.14010337286254337,
      -1.012376059460888, -1.3241578701223444, -2.718572313201977, -2.4726769096483445, -3.662889903151375]

o_eps = 1e-2
points = []
print()
for k in range(len(xs)):
    i = xs[k]
    j = ys[k]
    if -math.pi <= i + 2 * j <= 0:
        o_x_0 = np.array([i, j])
        res = second_order(func, der_func, der_der_func, o_x_0, o_eps)
        # print("[{:.3f}, {:.3f}]--[{:.4f}, {:.4f}]--{}".format(i, j, res[0][0], res[0][1], res[1]))
        points.append([i, j, res[1], res[0][0], res[0][1]])

print('eps: {}'.format(o_eps))
columns = ['x_0', 'y_0', 'iterations', 'x_opt', 'y_opt']
print(tabulate(points, headers=columns, floatfmt=".4f", tablefmt='github', showindex="always"))
