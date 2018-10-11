from tkinter import *
from itertools import islice
root = Tk()
root.title("Derivative Calculator")
root.geometry("450x115")
root.iconbitmap("favicon.ico")

#  Returns true if the string has a leading negative sign
def leadNeg(inExp):
    if inExp[0]=="-":
        print("negative coefficient")
        return True
    else:
        return False

#  Returns the coefficient given a string of a monomial function
def findCoeff(inExp):   
    tempCo = ""
    i = 0   
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

# Returns the exponent given a string of a monomial function
def findExp(inExp): 
    xLoc = inExp.find("x") 
    carrotLoc = inExp.find("^")     
    if xLoc == -1:
        tempExp = 0
    elif carrotLoc == -1:
        tempExp = 1
    else:
        tempExp = eval(inExp[inExp.find("^")+1:])       #Puts the part after "^" into tempExp, and executes any math involved, for example x^(3/2) will give 1.5
    return tempExp

""" 
Given an equation, a value of x, and two entries this function uses
the power rule to set the first entry to the mathematical formula for
the derivative, and the second entry to the calculated value of the
derivative at the given X value.
"""
def powerRule(inExp, x, derivEqEntry, derivEntry):      
    inExp.replace(" ","")           
    inExp.lower()                   
    coeff = findCoeff(inExp)            
    exp = findExp(inExp)                     
    dCoeff = float(coeff) * float(exp)
    dExp = float(exp - 1)
    derivFull = f"{dCoeff}"
    derivEntry.delete(0, "end")
    derivEqEntry.delete(0, "end")
    if dExp == 0:
        derivEqEntry.insert(0, derivFull)
        derivEntry.insert(derivFull)
    derivFull += f"x^{dExp}"
    
    derivEqEntry.insert(0, derivFull)
    derivEntry.insert(0, str(dCoeff*x**dExp))
     
#  Creates the main expression entry label and entry.
expressionLabel = Label(root, text="Enter an expression to derive(Ax^b)")
expressionLabel.grid(row=0, sticky=W)

expressionEntry = Entry(root, width=40)
expressionEntry.grid(row=0,column=1)

#  Creates the X value to derive at label and entry.
xValLabel = Label(root, text="Enter the value of X to derive at")
xValLabel.grid(row=1, sticky=W)

xValEntry = Entry(root, width=40)
xValEntry.grid(row=1, column=1)

# Creates the equation of the derivative and the final derived answer Labels and Entries
derivEqLabel = Label(root, text="Derivative Equation")
derivEqLabel.grid(row=3, column=0, sticky=W)

derivEqEntry = Entry(root, width=40)
derivEqEntry.grid(row=3, column=1)

derivLabel = Label(root, text="Solved Derivative")
derivLabel.grid(row=4, column=0, sticky=W)

derivEntry = Entry(root, width=40)
derivEntry.grid(row=4, column=1)

#  Creates the button used to derive, calls powerRule().
deriveButton = Button(root, text="Derive",command=lambda: (
    powerRule(
    str(expressionEntry.get()),float(xValEntry.get()), derivEqEntry, derivEntry)))
deriveButton.grid(columnspan=3, row=2, sticky=W)
deriveButton.config(width= 61, bg="grey")


root.mainloop()





