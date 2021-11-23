from sympy import parse_expr, symbols
def secant_eq(equ, x_prev, x_curr, iter, prec):
    x = symbols("x")    
    it_dic = {}
    fn = parse_expr(equ)
    num_of_iter = 0
    x_next = 0
    for i in range(iter):
        num_of_iter += 1
        f_x_curr = fn.subs(x, x_curr)
        f_x_prev = fn.subs(x, x_prev)
        x_next = x_curr - ((f_x_curr * (x_prev - x_curr))/(f_x_prev - f_x_curr))
        calc_prec = abs((x_next-x_curr)/x_next) * 100
        if calc_prec < prec:
            it_dic[i] = [x_next, x_curr, x_prev, calc_prec]
            break
        it_dic[i] = [x_next, x_curr, x_prev, calc_prec]
        x_prev = x_curr
        x_curr = x_next


    return[it_dic, x_next, equ, iter, prec, num_of_iter,'secant']


fn_eq = "x**2+x-6"
res = secant_eq(equ=fn_eq, x_prev=1, x_curr=1.1, iter=50, prec=0.03)
# print(res[0])
print(res[1])


        



