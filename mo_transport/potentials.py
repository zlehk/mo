import numpy as np

"""4 разные задачи"""

# costs = np.array([[4, 5, 2, 3],
#                   [1, 3, 6, 2],
#                   [6, 2, 7, 4]])
#
# supply = np.array([60, 100, 120])
# demand = np.array([30, 100, 40, 110])
#
# costs = np.array([[4, 11, 3, 12, 9],
#                   [7, 15, 7, 19, 17],
#                   [8, 13, 9, 15, 13],
#                   [2, 9, 3, 15, 8]])
#
# supply = np.array([16, 5, 14, 15])
# demand = np.array([7, 16, 9, 5, 13])

# costs = np.array([[20, 30, 40],
#                   [30, 70, 70]])
#
# supply = np.array([15, 5])
# demand = np.array([6, 9, 5])

"""Это наше Итоговое задание"""
costs = np.array([[40, 20, 80, 50, 0],
                  [30, 30, 60, 40, 0],
                  [50, 30, 40, 40, 0]])
supply = np.array([10000, 8000, 5000])
demand = np.array([4800, 4800, 6000, 5000, 2400])

n = len(supply)
m = len(demand)


def north_west():
    """Метод северо-западного угла"""
    route = np.zeros_like(costs)
    route_indexes = []
    u = v = 0
    s, d = np.zeros(n), np.zeros(m)
    while u <= n - 1 and v <= m - 1:
        if demand[v] - d[v] < supply[u] - s[u]:
            z = demand[v] - d[v]
            route[u][v] = z
            d[v] += z
            s[u] += z
            route_indexes.append([u, v])
            v += 1
        else:
            z = supply[u] - s[u]
            route[u][v] = z
            d[v] += z
            s[u] += z
            route_indexes.append([u, v])
            u += 1
    return [route, route_indexes]


def find_path(route_indexes, u, v):
    """Строим ломаную пересчета"""
    path = [[u, v]]
    if not look_horizontally(route_indexes, path, u, v, u, v):
        return None
    return path


def look_horizontally(route_indexes, path, u, v, u1, v1):
    """Поиск по горизонтали"""
    for i in range(0, m):
        if i != v and [u, i] in route_indexes:
            if i == v1:
                path.append([u, i])
                return True
            if look_vertically(route_indexes, path, u, i, u1, v1):
                path.append([u, i])
                return True
    return False


def look_vertically(route_indexes, path, u, v, u1, v1):
    """Поиск по вертикали"""
    for i in range(0, n):
        if i != u and [i, v] in route_indexes:
            if look_horizontally(route_indexes, path, i, v, u1, v1):
                path.append([i, v])
                return True
    return False


def set_potentials(route_indexes):
    """Рассчитываем потенциалы"""
    us = [None] * n
    vs = [None] * m
    us[0] = 0
    for i in range(0, len(route_indexes)):
        if vs[route_indexes[i][1]] is not None:
            us[route_indexes[i][0]] = vs[route_indexes[i][1]] - costs[route_indexes[i][0]][route_indexes[i][1]]
        elif us[route_indexes[i][0]] is not None:
            vs[route_indexes[i][1]] = us[route_indexes[i][0]] + costs[route_indexes[i][0]][route_indexes[i][1]]
        else:
            break
    return [us, vs]


def get_d_table(us, vs):
    """Таблица оценок"""
    ds = np.zeros_like(costs)
    for i in range(0, n):
        for j in range(0, m):
            ds[i][j] = us[i] + costs[i][j] - vs[j]
    return ds


def right_sort(route_indexes):
    """Зачем-то я расставляю в нужном мне порядке, уже не помню зачем"""
    new_route_indexes = [route_indexes[0]]
    used_us = set()
    used_us.add(route_indexes[0][0])
    used_vs = set()
    used_vs.add(route_indexes[0][1])
    for _ in range(1, len(route_indexes)):
        i = 1
        while route_indexes[i][0] not in used_us and route_indexes[i][1] not in used_vs:
            i += 1
        new_route_indexes.append(route_indexes[i])
        used_us.add(route_indexes[i][0])
        used_vs.add(route_indexes[i][1])
        route_indexes.pop(i)
    return new_route_indexes


def potentials():
    print("Метод СЕВЕРО-ЗАПАДНОГО УГЛА, начальное приближение:")
    [r, r_i] = north_west()
    print(r)

    print(costs)
    while True:
        [ui, vj] = set_potentials(r_i)

        dij = get_d_table(ui, vj)
        if len(np.extract(dij < 0, dij)) == 0:
            print("Условия оптимальности выполнены, оценки:")
            print(dij)
            print("Доп:")
            uui = np.reshape(ui, (n, 1))
            print(uui)
            print(vj)
            break

        ix, jy = np.argmin(dij) // m, np.argmin(dij) % m

        pth = find_path(r_i, ix, jy)

        route_path = []
        [route_path.append(r[pth[k][0]][pth[k][1]]) for k in range(0, len(pth))]

        uui = np.reshape(ui, (n, 1))
        print(uui)
        print(vj)
        print("Распределение:")
        print(r)
        print("Оценки:")
        print(dij)
        print("Линия пересчёта: ")
        for k in range(0, n):
            s = ""
            for t in range(0, m):
                if [k, t] in pth:
                    if pth.index([k, t]) % 2 == 0:
                        s += "[+] "
                    else:
                        s += "[-] "
                else:
                    s += "[ ] "
            print(s)
        print()

        route_path_minus_min = min(route_path[1::2])
        for k in range(0, len(route_path), 2):
            route_path[k] += route_path_minus_min
        for k in range(1, len(route_path), 2):
            route_path[k] -= route_path_minus_min

        zero_indexes = [k for k in range(len(route_path)) if route_path[k] == 0 and k % 2 == 1]

        if len(zero_indexes) == 1:
            zero_indexes_for_delete = zero_indexes
        else:
            zero_indexes_for_delete = [zero_indexes[0]]

        for k in range(len(pth)):
            if k in zero_indexes_for_delete:
                ind = r_i.index(pth[k])
                r_i[ind] = [ix, jy]
                r[pth[k][0], pth[k][1]] = 0
            else:
                r[pth[k][0], pth[k][1]] = route_path[k]

        r_i = right_sort(r_i)

    print("Оптимальное решение:")
    res = 0
    print(r)
    for k in range(len(r_i)):
        res += r[r_i[k][0], r_i[k][1]] * costs[r_i[k][0], r_i[k][1]]
    print("Полученная стоимость производства: {}".format(res))
