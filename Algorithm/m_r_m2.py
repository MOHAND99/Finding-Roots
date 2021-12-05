from sympy import parse_expr, symbols, diff


def multiple_root_mod_two(equ, x_curr, MAX_ITERS=50, prec=0.00001):
    x = symbols("x")    
    iters_data = []
    fn = parse_expr(equ)
    fn_derv = diff(fn, x)
    fn_second_derv = diff(fn_derv, x)
    num_of_iter = MAX_ITERS
    x_next = 0

    if fn_derv == 0:
        return "Error First Derv. Is Zero"

    if fn_second_derv == 0:
        return "Error Second Derv. Is Zero"

    iters_data.append(['Xi', 'Xi+1' , 'Precession'])

    calc_prec = 0   
    for i in range(MAX_ITERS):
        f_x_curr = fn.subs(x, x_curr)
        f_x_derv = fn_derv.subs(x, x_curr)
        f_x_sec_derv = fn_second_derv.subs(x, x_curr)
        round_digit = 6
        if x_next == 0:
            break
        x_next = x_curr - ((f_x_curr * f_x_derv) / ((f_x_derv**2)-(f_x_curr * f_x_sec_derv)))
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        iters_data.append([round(x_curr, round_digit), round(x_next, round_digit),calc_prec])
        if calc_prec < prec:
            num_of_iter = i + 1
            break
        x_curr = x_next


    return [iters_data, x_next, equ, MAX_ITERS, prec, num_of_iter,'mr_second']