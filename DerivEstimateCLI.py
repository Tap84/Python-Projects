def findExp(eq):
    expLoc = eq.find("^")
    if expLoc > -1:   
        return eval(eq[expLoc+1:])
    else:
        return 1
def findCoeff(eq):
    xLoc = eq.find("x")
    if xLoc > -1:
        coeff = eq[:xLoc] 
    else:
        coeff = 1
    return coeff
def derive(eq,x,xStep):
    exp = findExp(eq)
    if eq.find("x") == -1:
        coeff = findCoeff(eq)
    else:
        coeff = eval(findCoeff(eq))
    if eq.find("x") > -1:
        finalApprox = ((coeff * (x+xStep) ** exp) - (coeff * x ** exp)) / xStep
    else:
        finalApprox = coeff
    print(format(finalApprox,".4f"))

equation = input("Enter a simple monomial expression in the form (Ax^b)")
xVal = float(input("Enter the value of X to solve the equation at"))
xStep = float(input("Enter the precision you want the derivative to be taken at, the smaller number the more accurate, something like 0.0001 is very accurate"))
derive(equation,xVal,xStep)
