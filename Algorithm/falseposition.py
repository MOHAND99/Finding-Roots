from sympy import parse_expr , symbols

def falsePosition(equ,start,end,Max_ITR= 50,prec = 0.00001):
    
    func = parse_expr(equ)
    x = symbols('x')
   
    numberOfIterations = Max_ITR
    iterationData = []

    if func.subs(x,start) * func.subs(x,end) >= 0:
        print("Assumed a and b are not correct")
        return -1

    c = 0
    old_c = 0

    for i in range(Max_ITR):

        c = (start * func.subs(x,end) - end * func.subs(x,start)) / func.subs(x,end) - func.subs(x,start)
        calculatedPrec = abs((c-old_c)/c) * 100
        iterationData[i] = [start ,func.subs(x,start) ,end ,func.subs(x,end) ,c ,func.subs(x,c)]

        if func.subs(x,c) == 0 or calculatedPrec < prec:
           
            if func.subs(x,c) != 0:
                prec = calculatedPrec
           
            else:
                prec = 0
            
            numberOfIterations = i + 1
            break
        
        elif func.subs(x,c) * func.subs(x,start) < 0:
                end = c
        
        else:
            start = c

        return [iterationData,equ,Max_ITR,numberOfIterations,prec,"FALSE POSITION"]
        
