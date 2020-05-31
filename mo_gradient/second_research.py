import numpy as np
from mo_gradient.funcs import func, der_func, der_der_func, norm2
from tabulate import tabulate


def second_order_research(f, df, ddf, x_0, eps, e=0.47, x_opt=np.array([-1.31593273, -0.31593273])):
    x = x_0
    norms = [norm2(x - x_opt)]
    xs = [x]
    while norm2(df(x)) ** 2 >= eps:
        alpha = 1
        p = -1 * np.dot(np.linalg.inv(ddf(x)), df(x))
        x_next = x + alpha * p
        while f(x_next) - f(x) > e * alpha * np.dot(df(x), p):
            alpha /= 2
            x_next = x + alpha * p
        x = x_next
        norms.append(norm2(x - x_opt))
        xs.append(x)
    return [xs, norms, x_opt]


o_eps = 0.01
ips = [-0.6799281866848323, 2.420223444760598, 4.388096788407111]  # , 10.0, 25.0]
jps = [-0.14010337286254337, -2.718572313201977, -2.4726769096483445]  # , -10.0, -23.0]

print()
columns = ['k', 'x_k', 'x_k+1', '||x_k - x_opt||', '||x_k+1 - x_opt||', '||x_k - x_opt||^gamma', 'C>=']
for k in range(len(ips)):
    points = []
    i = ips[k]
    j = jps[k]
    o_x_0 = np.array([i, j])
    gamma = 2
    print("x_0: [{:.3f}, {:.3f}]\ngamma: {}".format(i, j, gamma))
    res = second_order_research(func, der_func, der_der_func, o_x_0, o_eps)
    print("x_opt: [{:.3f}, {:.3f}]".format(res[2][0], res[2][1]))
    for t in range(len(res[1]) - 1):
        points.append(['[{:.3f},{:.3f}]'.format(res[0][t][0], res[0][t][1]),
                       '[{:.3f},{:.3f}]'.format(res[0][t + 1][0], res[0][t + 1][1]),
                       res[1][t],
                       res[1][t + 1],
                       res[1][t] ** gamma,
                       res[1][t + 1] / (res[1][t] ** gamma)])
    print(tabulate(points, headers=columns, floatfmt=".4f", tablefmt='github', showindex="always"))
    print()
