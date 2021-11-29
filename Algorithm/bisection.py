from sympy import parse_expr, symbols


def bisection(f_str, start, end, MAX_ITERS=50, prec=0.00001):
    f = parse_expr(f_str)
    x = symbols('x')

    if f.subs(x, start)*f.subs(x, end) > 0:
        return "Bisection method fails."

    old_mid = 0
    mid = 0
    num_of_iters = 0
    iters_data = []

    for i in range(MAX_ITERS):
        mid = (start + end)/2
        f_mid = f.subs(x, mid)

        calc_prec = abs((mid-old_mid)/mid) * 100
        iters_data.append([start, end, mid, calc_prec])

        if calc_prec < prec or f_mid == 0:
            prec = calc_prec if f_mid != 0 else 0
            num_of_iters = i + 1
            break
        elif f.subs(x, start)*f_mid < 0:
            end = mid
        elif f.subs(x, end)*f_mid < 0:
            start = mid

        else:
            return "Bisection method fails."

        old_mid = mid

    return [iters_data,
            mid,
            f_str,
            # boolean refer to return cause
            # MAX_ITER / reach acceptable precision
            num_of_iters != MAX_ITERS,
            prec,
            num_of_iters,
            'bisection']
