from Consts import *
from Fixer import *

#check if the string is a Number
def isNum(num : str):
    try:
        float(num)
        return True
    except ValueError:
        return False


#only valid chars
def onlyAllowdCharsValidation(l: list):
    for i in l:
        if not i.isdecimal():
            if not AllowedList.count(i) == 1:
                return False
    return True

#no num *space* nun
def noDigSpacDigValidation(l: list):
    tempBack = ''
    i = 0
    while i < len(l):
        if (l[i] == " " and i > 0):
            tempBack = l[i - 1]
            while (l[i] == " " and i < len(l) - 1):
                i = i + 1
        if ((tempBack.isdigit() or isinstance(tempBack , float)) and (l[i].isdigit() or isinstance(l[i],float))):
            return False
        if (OperatorList.count(l[i]) == 1):
            tempBack = ''
        i = i + 1
    return True

#both of the above + .. validator
def AllowedAndNoDigSpaceValid(l: list):
    if (onlyAllowdCharsValidation(l) == False):
        print("a non valid char was inputed!")
    if (noDigSpacDigValidation(l) == False):
        print("you cant space between two numbers!")
    return onlyAllowdCharsValidation(l) and noDigSpacDigValidation(l)  and noDoubleDot(l)

# no - *space* num
def noMinusSpaceDig(l : list):
    flag = True
    for i in range(len(l) - 1):
        if l[i] == ' ':
            if isNum(l[i - 1]) and isNum(l[i + 1]):
                flag = False
            elif l[i - 1] == '-' and isNum(l[i + 1]):
                if i == 1:
                    flag = False
                else:
                    if l[i - 2] == ' ':
                        if l[i - 3] in regularOperator or \
                                l[i - 3] in unregularOperator or \
                                l[i - 3] == '(':
                            flag = False
                    elif l[i - 2] in regularOperator or \
                            l[i - 2] in unregularOperator or \
                            l[i - 2] == '(':
                        flag = False
    if (flag == False):
        print("you canot put a space between minus and number without operator on the other side!")
    return flag

# validation for close and open ( )
def checkValidParenthesisOpenAndClose(l : list):
    count = 0
    for i in range(len(l)):
        if l[i] == '(':
            count = count + 1
        elif l[i] == ')':
            count = count - 1
        if (count < 0):
            print("unvalid close and open Parenthesis")
            return False
    if (count==0):
        return True
    else:
        print("unvalid close and open Parenthesis")


#validation for no ()
def noEmptyParenthesis(l : list):
    for i in range(len(l) - 1):
        if (l[i] == '(' and l[i+1] == ')'):
            print("you cant leave Parenthesis empty!")
            return False
    return True

def noDoubleDot(l : list):
    for i in range(len(l) - 1):
        if (l[i] == '.' and l[i+1] == '.'):
            print("you cant have two dots next to each other")
            return False
    return True

#both of the ( ) validation together
def ParenthesisValidation(l : list):
    return noEmptyParenthesis(l) and checkValidParenthesisOpenAndClose(l)


#check there is no double regular operator (except minus , he is a spaciel case)
def regularOperatorValidator(l : list):
    for i in range(len(l) - 1):
        if (l[i] in regularOperatorNoMinus and l[i+1] in regularOperatorNoMinus):
            print("you cant have two regular operators next to each other")
            return False
    if l[len(l) - 1] in regularOperator:
        print("you cant end with regular operator!")
        return False
    return True

#check the is no minus Unsined to number (minus of subtraction) before operator
def noMinusBeforeRegularOperator(l : list):
    for i in range(len(l) - 1):
        if (l[i] == '-' and l[i+1] in regularOperatorNoMinus):
            print("you cant have minus before another regular operator")
            return False
    return True

#check that after leftOperators can come only num , - or (     also check there is something after it
def leftOperatorsValidatorFromRight(l : list):
    for i in range(len(l) - 1):
        if (l[i] in leftOperators):
            if (l[i+1] == '-'):
                if (i+2 >= len(l)):
                    print("if after tilda comes a - , the next input must be a number")
                    return False
                elif not isNum(l[i + 2]):
                    print("if after tilda comes a - , the next input must be a number")
                    return False
            if (l[i+1] in regularOperatorNoMinus):
                print("after tilda must come a number or (")
                return False
    if (l[(len(l) -1)]) in leftOperators:
        print("tilda canot end the equation")
        return False
    return True


#check that before leftOperators can come only regular operators
def leftOperatorsValidatorFromLeft(l : list):
    for i in range(len(l) - 1):
        if (not l[i] in regularOperator) and l[i+1] in leftOperators:
            if (l[i] != '('):
                print("must have operator before tilda unless its the starting element")
                return False
    return True


#check that after rightOperator can come only regular operators
def RightOperatorsValidatorFromRight(l : list):
    for i in range(len(l) - 1):
        if (l[i] in rightOperators) and (not l[i+1] in regularOperator) and (l[i+1] != ')') and (not l[i+1] in rightOperators):
            print("must have operator after rightOperator")
            return False
    return True


#check that before rightOperator can come only number or )

def RightOperatorsValidatorFromLeft(l : list):
    for i in range(len(l)-1):
        if ((l[i+1] in rightOperators and not (isNum(l[i]) or l[i] == ')' or l[i] in rightOperators))):
            print("before rightOperator must come a number or something that will preduce a number")
            return False
    if (l[0] in rightOperators):
        print("before rightOperator must come a number")
        return False
    return True

def allOperatorValidation(l : list):
    return regularOperatorValidator(l) and noMinusBeforeRegularOperator(l) and leftOperatorsValidatorFromRight(l) and leftOperatorsValidatorFromLeft(l) and RightOperatorsValidatorFromRight(l) and RightOperatorsValidatorFromLeft(l)

