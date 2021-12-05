from sympy import parse_expr, symbols


def secant_eq(equ, x_prev, x_curr, MAX_ITERS=50, prec=0.00001):

    x = symbols("x")
    iters_data = []
    fn = parse_expr(equ)
    num_of_iters = MAX_ITERS
    x_next = 0
    iters_data.append(['Xi-1', 'Xi', 'Xi+1' , 'Precession'])

    for i in range(MAX_ITERS):
        f_x_curr = fn.subs(x, x_curr)
        f_x_prev = fn.subs(x, x_prev)
        digits_after_point = 6
        x_next = x_curr -((f_x_curr * (x_prev - x_curr))/(f_x_prev - f_x_curr))
        if x_next == 0:
            break
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        iters_data.append([round(x_prev, digits_after_point),
                           round(x_curr, digits_after_point),
                           round(x_next, digits_after_point),
                           calc_prec])

        if calc_prec < prec:
            num_of_iters = i + 1
            break

        x_prev = x_curr
        x_curr = x_next

    return [iters_data,
            x_next,
            equ,
            # boolean refer to return cause
            # MAX_ITER / reach acceptable precision
            MAX_ITERS,
            prec,
            num_of_iters,
            'secant']
