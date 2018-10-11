from itertools import islice
def leadNeg(inExp): #Tests if there is a leading negative in a string, returns T/F
    if inExp[0]=="-":
        print("negative coefficient")
        return True
    else:
        return False
def findCoeff(inExp):   #Finds the coefficient given an expression
    tempCo = ""
    i = 0   #Position in inExp
    if leadNeg(inExp):
        tempCo += "-"
        i += 1  #Moving to after minus
        if inExp[1] == "x": #If input is "-x"
            return "-1"
    if inExp[0] == "x": #If input is "x"
        return "1"
    for char in islice(inExp, i, None):    #Efficient slice, [islice( {listName} , {startIndex} , {endIndex} )]
        if char == "x":
            break
        tempCo += char
        
    return tempCo
def findExp(inExp): #Finds the exponent given an expression
    # tempExp = ""
    xLoc = inExp.find("x")  #Find position of x
    carrotLoc = inExp.find("^") #Find position of carrot
    if carrotLoc == -1:
        tempExp = 1 
    else:
        tempExp = eval(inExp[inExp.find("^")+1:])   #Puts the part after "^" into tempExp, and executes any math involved, for example x^(3/2) will give 1.5
    return tempExp
def powerRule(inExp, x):   #Execute power rule, print derivative and return value at x
    inExp.replace(" ","")  #Remove Spaces
    inExp.lower()  #Convert to lower case
    coeff = findCoeff(inExp)        #Gets the Coefficient of the given expression using findCoeff()
    exp = findExp(inExp)            #Gets the exponent of the given expression using findExp()
    dCoeff = float(coeff) * float(exp)  #
    dExp = float(exp) - 1             #
    derivFull = f"{dCoeff}"
    if dExp == 0:   #If given "x^1" 
        return derivFull
    derivFull += f"x^{dExp}"
    print(f"The Derivative of {inExp} is {derivFull}")
    return dCoeff*x**dExp    #Final
while(True):
    expression = input("Enter the polynomial expression to derive in the form (ax^b)\n> ")     #Input String
    
    xVar = float(input("Enter the value of x you wish to derive the expression at\n> "))

    derivValue = powerRule(expression,xVar)
    print(f"At x = {xVar}, the derivative of {expression} is {derivValue}")
    continuePrompt = input("Would you like to continue? If not type \"exit\"\n> ")
    if continuePrompt.lower() == "exit":
        break


