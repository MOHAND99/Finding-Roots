from sympy import parse_expr, symbols, diff


def newton_eq(equ, x_curr, MAX_ITERS=50, prec=0.00001):
    x = symbols("x")    
    iters_data = {}
    fn = parse_expr(equ)
    fn_d = diff(fn, x)
    num_of_iter = 0
    x_next = 0
    
    if fn_d == 0:
        return "Error"
        
    calc_prec = 0   
    for i in range(iter):
        f_x_curr = fn.subs(x, x_curr)
        f_x_derv = fn_d.subs(x, x_curr)
        round_digit = 6
        x_next = x_curr - (f_x_curr / f_x_derv)
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        iters_data[i] = [round(x_curr, round_digit), round(x_next, round_digit),calc_prec]
        if calc_prec < prec:
            num_of_iter = i
            break
        x_curr = x_next


    return [iters_data, x_next, equ, MAX_ITERS, prec, num_of_iter+1,'newton']
