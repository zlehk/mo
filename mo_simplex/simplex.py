import numpy as np
from numpy import linalg as la
from itertools import combinations


def enum_method(n, m, a_matrix, b):
    """Метод перебора"""
    print("Ищем начальное приближение МЕТОДОМ ПЕРЕБОРА:")
    x_0 = np.zeros(n)
    for comb in combinations(range(n), m):
        matrix = np.take(a_matrix, comb, axis=1)
        if la.det(matrix) and np.amin(la.solve(matrix, b)) >= 0:
            np.put(x_0, comb, la.solve(matrix, b))
            break
    return x_0


def artificial_basis_method(n, m, a_matrix, b):
    """Метод искусственного базиса"""
    print("Ищем начальное приближение МЕТОДОМ ИСКУССТВЕННОГО БАЗИСА:")
    c = np.concatenate([np.zeros(n), np.ones(m)])
    x_0 = np.concatenate([np.zeros(n), b])
    new_a_matrix = np.column_stack((a_matrix, np.eye(m)))
    return simplex(n + m, m, new_a_matrix, c, x_0)[0:n]


def get_new_b_matrix(b_matrix, u_k, n_k, i_k):
    """Вычисление матрицы B через ее предыдущее значение"""
    f_matrix = np.zeros_like(b_matrix)
    np.fill_diagonal(f_matrix, 1)
    i_k_column = (-1 * np.divide(u_k[n_k], u_k[i_k]))
    i_k_column[np.where(n_k == i_k)[0][0]] = np.divide(1, u_k[i_k])
    f_matrix[:, np.where(n_k == i_k)[0][0]] = i_k_column
    return np.dot(f_matrix, b_matrix)


def simplex(n, m, a_matrix, c, x_0):
    """Симплекс_метод, передаем вычисленное ранее начальное приближение"""
    n_k_plus = np.where(x_0 > 1.0e-10)[0]
    n_k_zero = np.where(np.fabs(x_0) < 1.0e-10)[0]
    n_k_plus_extra = np.empty(m - n_k_plus.size)

    if n_k_plus_extra.size > 0:
        for comb in combinations(n_k_zero, n_k_plus_extra.size):
            matrix = np.take(a_matrix, np.append(n_k_plus, comb), axis=1)
            if la.det(matrix):
                n_k_plus_extra = np.array(comb)
                break
    n_k = n_k_plus if not n_k_plus_extra.size else np.sort(np.block([n_k_plus, n_k_plus_extra]))
    l_k = np.array(list(set(range(n)) - set(n_k)))

    b_matrix = la.inv(np.take(a_matrix, n_k, axis=1))

    x_k = x_0
    solution = None
    n_k_prev = np.array([], dtype='int64')
    swap_history = []

    while solution is None:
        d_k = np.take(c, l_k) - np.dot(np.take(c, n_k),
                                       np.dot(b_matrix, np.take(a_matrix, l_k, axis=1)))

        if d_k[d_k < 0].size == 0:
            # print("We've found optimal solution!")
            solution = x_k
            break  # BIG BREAK

        np.place(d_k, d_k >= 0, np.amin(d_k) - 1)  # выгодно брать минимальное по модулю
        j_k = np.take(l_k, np.argmax(d_k))

        u_k = np.zeros(n)
        np.put(u_k, n_k, np.dot(b_matrix, np.take(a_matrix, j_k, axis=1)))
        np.put(u_k, j_k, -1)

        if u_k[u_k > 0].size == 0:
            print("Function is not limited from below!")
            solution = np.array([])  # просто заглушка
            break  # BIG BREAK

        i_k = -1

        if n_k is n_k_plus or np.amax(np.take(u_k, n_k_plus_extra)) <= 0:
            n_k_plus_u_k_plus = np.extract(u_k[n_k_plus] > 0, n_k_plus)
            theta = np.amin(np.divide(x_k[n_k_plus_u_k_plus], u_k[n_k_plus_u_k_plus]))
            i_k = n_k_plus_u_k_plus[np.argmin(np.divide(x_k[n_k_plus_u_k_plus], u_k[n_k_plus_u_k_plus]))]
            x_k = np.subtract(x_k, theta * u_k)

            n_k_prev = np.append(n_k_prev, n_k)
            np.put(n_k_plus, np.where(n_k_plus == i_k)[0], j_k)
            n_k = n_k_plus
            l_k = np.array(list(set(range(n)) - set(n_k)))

            swap_history = []

        else:
            def columns_for_swap():
                for old in n_k_plus_extra:
                    for new in l_k:
                        yield old, new

            for i, j in columns_for_swap():
                if (i, j) in swap_history or (j, i) in swap_history:
                    continue
                n_k_plus_extra_attempt = np.array(n_k_plus_extra)
                np.put(n_k_plus_extra_attempt, np.where(n_k_plus_extra_attempt == i)[0], j)

                if la.det(np.take(a_matrix, np.append(n_k_plus, n_k_plus_extra_attempt), axis=1)):
                    swap_history.append((i, j))
                    n_k_plus_extra = n_k_plus_extra_attempt
                    n_k_prev = np.append(n_k_prev, n_k)
                    np.put(n_k, np.where(n_k == i)[0], j)
                    l_k = np.array(list(set(range(n)) - set(n_k)))
                    i_k = i
                    break

        b_matrix = get_new_b_matrix(b_matrix, u_k, n_k_prev, i_k)
        n_k_prev = np.delete(n_k_prev, np.s_[:])

    return solution


def calculate_by_simplex_method(a_matrix, b, c, init_approx_method):
    """Решение задачи минимизации симплекс-методом, метод для выбора начального приближения передаем"""
    n, m = len(c), len(b)
    x_0 = init_approx_method(n, m, a_matrix, b)
    print("initial approximation: {}".format(x_0))
    print("x_0: {}".format(x_0))
    x_opt = simplex(n, m, a_matrix, c, x_0)[0:n]
    print("optimal solution: {}".format(x_opt))
    print("x_opt: {}".format(x_opt[0:m]))
    print("target function: {}".format(np.dot(c, x_opt)))
    print('\n')
    return [x_opt, np.dot(c, x_opt)]
