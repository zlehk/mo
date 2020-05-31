import numpy as np
from mo_simplex.simplex import calculate_by_simplex_method
from mo_simplex.simplex import enum_method, artificial_basis_method

""" те же 4 задачи, но записанные в форме для симплекс метода """
""" АХТУНГ, нужно убрать в матрице s_a любую одну строку, а в векторе s_b соответствующий ей по порядку элемент """

# s_a = np.array([[1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
#                 [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
#                 [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1]])
# s_b = np.array([60, 100, 120, 30, 100, 40, 110])
# s_c = np.array([4, 5, 2, 3,
#                 1, 3, 6, 2,
#                 6, 2, 7, 4])

# s_a = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
#                 [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
#                 [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
#                 [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
#                 [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
#                 [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]], dtype='int64')
# s_b = np.array([16, 5, 14, 15, 7, 16, 9, 5, 13])
# s_c = np.array([4, 11, 3, 12, 9,
#                 7, 15, 7, 19, 17,
#                 8, 13, 9, 15, 13,
#                 2, 9, 3, 15, 8])


# s_a = np.array([[1, 1, 1, 0, 0, 0],
#                 [0, 0, 0, 1, 1, 1],
#                 [1, 0, 0, 1, 0, 0],
#                 [0, 1, 0, 0, 1, 0],
#                 [0, 0, 1, 0, 0, 1]])
# s_b = np.array([15, 5, 6, 9, 5])
# s_c = np.array([20, 30, 40,
#                 30, 40, 70])

"""Это наше Итоговое задание"""
s_a = np.array([[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1]], dtype='int64')
s_b = np.array([8000, 5000, 4800, 4800, 6000, 5000, 2400])
s_c = np.array([40, 20, 80, 50, 0,
                30, 30, 60, 40, 0,
                50, 30, 40, 40, 0])


res = calculate_by_simplex_method(s_a, s_b, s_c, artificial_basis_method)
print("Решение траспортной задачи СИМПЛЕКС-МЕТОДОМ: ")
print("x_opt: {}".format(np.array(res[0], dtype='int64')))
print("Стоимость производства: {}".format(res[1]))
