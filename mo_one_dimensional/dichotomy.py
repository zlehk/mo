def dichotomy_method(a, b, eps, func):
    delta = eps * 0.1
    func_call_counter = 0
    x = 0
    data = []
    while True:
        x_1 = (a + b) / 2 - delta
        x_2 = (a + b) / 2 + delta
        f_x_1 = func(x_1)
        f_x_2 = func(x_2)
        if (b - a) <= eps:
            data.append((a, b, None, None, None, None, b - a))
            break
        else:
            data.append((a, b, x_1, x_2, f_x_1, f_x_2, b - a))
        if f_x_1 <= f_x_2:
            b = x_2
            x = x_1
        else:
            a = x_1
            x = x_2
        func_call_counter += 2
    return [x, func(x), func_call_counter, data]
