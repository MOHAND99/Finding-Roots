from sympy import parse_expr, symbols

def fixed_pt(equ, x_curr, MAX_ITERS=50, prec=0.00001):
    x = symbols("x")    
    iters_data = {}
    fn = parse_expr(equ)
    num_of_iter = MAX_ITERS
    x_next = 0

        
    calc_prec = 0   
    for i in range(MAX_ITERS):
        f_x_curr = fn.subs(x, x_curr)
        round_digit = 6
        x_next = f_x_curr
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        iters_data[i] = [round(x_curr, round_digit), round(x_next, round_digit), calc_prec]
        if calc_prec < prec:
            num_of_iter = i + 1
            break
        x_curr = x_next


    return [iters_data, x_next, equ, MAX_ITERS, prec, num_of_iter,'fixed_pt']
