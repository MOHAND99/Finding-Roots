from sympy import parse_expr, symbols, diff


def multiple_root_mod_one(equ, x_curr, m, MAX_ITERS=50, prec=0.00001):
    x = symbols("x")    
    iters_data = []
    fn = parse_expr(equ)
    fn_derv = diff(fn, x)
    num_of_iter = MAX_ITERS
    x_next = 0

    if fn_derv == 0:
        return "Error First Derv. Is Zero"
    iters_data.append(['Xi', 'Xi+1' , 'Precession'])
    calc_prec = 0   
    for i in range(MAX_ITERS):
        f_x_curr = fn.subs(x, x_curr)
        f_x_derv = fn_derv.subs(x, x_curr)
        round_digit = 6
        x_next = x_curr - (m * (f_x_curr / f_x_derv))
        calc_prec = abs((x_next-x_curr)/x_next) 
        iters_data.append([round(x_curr, round_digit), round(x_next, round_digit),calc_prec])
        if calc_prec < prec:
            num_of_iter = i + 1
            break
        x_curr = x_next


    return [iters_data, x_next, equ, MAX_ITERS, prec, num_of_iter,'mr_first']