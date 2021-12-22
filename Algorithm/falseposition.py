from sympy import parse_expr , symbols

def falsePosition(equ,start,end,Max_ITR= 50,prec = 0.00001):
    
    x = symbols("x")
    func = parse_expr(equ)
   
    numberOfIterations = Max_ITR
    iterationData = []

    if func.subs(x,start) * func.subs(x,end) >= 0:
        print("Assumed a and b are not correct")
        return -1

    c = 0
    old_c = 0
    iterationData.append(['Xl','Xu','Xr','Prec'])
    for i in range(Max_ITR):
        round_digit = 6
        c = (start * func.subs(x,end) - end * func.subs(x,start)) / (func.subs(x,end) - func.subs(x,start))

        if c == 0:
            break

        calculatedPrec = abs((c-old_c) / c)
        iterationData.append([round(start,round_digit) ,round(end,round_digit) , round(c,round_digit),calculatedPrec])

        if func.subs(x, c) == 0 or calculatedPrec < prec:
           
            if func.subs(x,c) != 0:
                prec = calculatedPrec
           
            else:
                prec = 0
            
            numberOfIterations = i + 1
            break
        
        if func.subs(x, c)  < 0:
            end = c
        
        else:
            start = c

        old_c = c
    return [iterationData, c, equ,Max_ITR, numberOfIterations,prec,"FALSE POSITION"]
        
# a =  falsePosition("x ** 3  - 3 * x + 1", 0, 1, 50, 0.000001)
# for i in a[0]:
#     print(i)
# print(a[1])
