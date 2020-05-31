import numpy as np
from numpy import linalg as la

n = 4


def func(x):
    """x^2 + 2xy + 4y^2 + 2z^2 + 4yz + w^2"""
    return x[0] ** 2 + 2 * x[0] * x[1] + 4 * (x[1] ** 2) + 2 * (x[2] ** 2) + 4 * x[1] * x[2] + x[3] ** 2


def der_func(x):
    return np.array([2 * x[0] + 2 * x[1],
                     2 * x[0] + 8 * x[1] + 4 * x[2],
                     4 * x[2] + 4 * x[1],
                     2 * x[3]])


def eqs():
    return {'left': np.array([[1, 0, -3, 4],
                              [0, 4, -3, 6]]),
            'right': np.array([[8],
                               [0]])}


def ineqs():
    return {'left': np.array([[2, -3, 2, 3],
                              [-2, 5, 3, -5]]),
            'right': np.array([[7],
                               [6]])}


spec_ineqs = ineqs()['right']
# spec_ineqs[0] -= 1
spec_ineqs[1] -= 1
x_0 = la.solve(np.row_stack((eqs()['left'], ineqs()['left'])), np.row_stack((eqs()['right'], spec_ineqs)))

C = np.array([[1, 0, -3, 4],
              [0, 4, -3, 6]])
d = np.array(np.array([[8],
                       [0]]))
F = np.array([[2, -3, 2, 3],
              [-2, 5, 3, -5]])
g = np.array([[7],
              [6]])

alpha0 = 0.25
lambd = 0.5

x_k = x_0
x_opt = 0

while True:
    F1, g1 = np.empty((0, 4)), np.empty((0, 1))
    F2, g2 = np.empty((0, 4)), np.empty((0, 1))

    for i in range(np.size(F, axis=0)):
        if g[i] - np.dot(F[i], x_0) <= 1e-10:
            F1 = np.append(F1, [F[i]], axis=0)
            g1 = np.append(g1, [g[i]], axis=0)
        else:
            F2 = np.append(F2, [F[i]], axis=0)
            g2 = np.append(g2, [g[i]], axis=0)

    print("x_k:")
    print(x_k)
    A = np.row_stack((C, F1))
    print("A")
    print(A)
    P_k = np.eye(np.size(A, axis=1))
    A_med = la.inv(np.matmul(A, np.transpose(A)))
    if A.size != 0:
        P_k -= np.matmul(np.matmul(np.transpose(A), A_med), A)
    s_k = -np.matmul(P_k, der_func(x_k))
    print("s_k:{}".format(la.norm(s_k)))

    if la.norm(s_k) < 1e-9:
        print("s_k is ZERO")
        if A.size == 0:
            x_opt = x_k
            break
        else:
            w = -np.matmul(np.matmul(A_med, A), der_func(x_k))
            v, u = np.split(w, [np.size(C, axis=0)])

            if len(u[u < 0]) == 0:
                print("Find optimal solution")
                x_opt = x_k
                break
            else:
                for i in range(np.size(u, axis=0)):
                    if np.count_nonzero(u[i][0]) < 0:
                        F1 = np.delete(F1, i, axis=0)
                        g1 = np.delete(g1, i, axis=0)
                        A = np.row_stack((C, F1))
                        break
                break
    alpha_k = 0
    reps_less, reps_more = 0, 0
    k = 0
    k_more, k_less = 0, 0
    alpha_k_less = alpha0 * (lambd ** k)
    alpha_k_more = alpha0 * (lambd ** k)
    while (np.all(np.dot(F2, x_k + alpha_k_less * s_k) > g2) and func(x_k + alpha_k_less * s_k) >= func(x_k)) \
            and reps_less < 100:
        k += 1
        alpha_k_less = alpha0 * (lambd ** k)
        alpha_k_more = alpha0 * (lambd ** -k)
        reps_less += 1

    alpha_k = alpha_k_less
    if reps_less == 100:
        print("ACHTUNG")
        x_opt = x_k
        break

    x_k_next = x_k + alpha_k * s_k
    x_k = x_k_next

print("x_opt:")
print(x_opt)
