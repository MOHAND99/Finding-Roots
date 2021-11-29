from sympy import parse_expr, symbols


def secant_eq(equ, x_prev, x_curr, iter=50, prec=0.00001):
    x = symbols("x")
    iter_data = {}
    fn = parse_expr(equ)
    num_of_iter = 0
    x_next = 0

    for i in range(iter):
        f_x_curr = fn.subs(x, x_curr)
        f_x_prev = fn.subs(x, x_prev)
        digits_after_point = 6
        x_next = round(
                        x_curr -
                        ((f_x_curr * (x_prev - x_curr))/(f_x_prev - f_x_curr)),
                        digits_after_point)

        calc_prec = abs((x_next-x_curr)/x_next) * 100
        iter_data[i] = [x_prev, x_curr, x_next, calc_prec]
        if calc_prec < prec:
            prec = calc_prec
            num_of_iter = i + 1
            break

        x_prev = x_curr
        x_curr = x_next

    num_of_iter = num_of_iter if num_of_iter != 0 else iter

    return [iter_data,
            x_next,
            equ,
            # boolean refer to return cause
            # MAX_ITER / reach acceptable precision
            iter != num_of_iter,
            prec,
            num_of_iter,
            'secant']
