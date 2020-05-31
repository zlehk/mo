def golden_ration_method(a, b, eps, func, gamma=(1 + 5 ** 0.5) / 2):
    delta = b - a
    x = 0
    data = []
    c = a + delta / (gamma ** 2)
    d = a + delta / gamma
    func_c, func_d = func(c), func(d)
    func_call_counter = 1
    delta /= gamma
    while delta > eps:
        data.append((a, b, delta, c, d, func_c, func_d))
        delta /= gamma
        if func_c <= func_d:
            b, d, x = d, c, c
            c = a + delta / gamma
            func_d, func_c = func_c, func(c)
        else:
            a, c, x = c, d, d
            d = a + delta
            func_c, func_d = func_d, func(d)
        func_call_counter += 1
    data.append((a, b, delta, None, None, None, None))
    return [x, func(x), func_call_counter, data]
