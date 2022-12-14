import math
from Fixer import *
from Consts import *
from allExceptions import *


def copyLList(l : list):
    temp = []
    for i in range(len(l)):
        temp.append(l[i])
    return temp

def getOperatorList(f : int):
    temp = []
    for k, v in OperatorDict.items():
        if v == f:
            temp.append(k)
    return temp

def removeDecimal(f: float) -> int:
    s = str(f)
    s = s.replace('.', '')
    try :
        int(s)
    except:
        raise numberToBig
    return int(s)

def factorial(f : float):
    if (f == 0):
        return 0
    if (f < 0):
        raise NegetiveFactorialException
    sum = 1
    if (float(f).is_integer()):
        while (f > 1):
            sum = sum * f
            f = f - 1
    else:
        raise floatFactorial
    return sum

def sumOfDig(f : float):
    temp = removeDecimal(f)
    sum = 0
    if (temp < 0):
        temp = - temp
    while (temp > 0):
        sum = sum + temp % 10
        temp = int(temp/10)
    return sum

def getMax(f1 : float , f2 : float):
    if (f1 > f2):
        return f1
    return f2

def getMin(f1 : float , f2 : float):
    if (f1 > f2):
        return f2
    return f1


def calculation(l : list):
    l = calculate6(l)
    l = calculate5(l)
    l = calculate4(l)
    l = calculate3(l)
    l = calculate2(l)
    l = calculate1(l)
    return l[0]

def calculate6(l : list):
    i = 0
    t = len(l)
    operators = getOperatorList(6)
    while i<t:
        if l[i] in rightOperators and l[i] in operators:
            while True:
                if l[i] == '!':
                    l[i-1] = factorial(l[i-1])
                    del l[i]
                    break
                elif l[i] == '#':
                    l[i - 1] = sumOfDig(l[i - 1])
                    del l[i]
                    break
        elif l[i] in leftOperators and l[i] in operators:
            if l[i] == '~':
                l[i + 1] =  -(l[i + 1])
                del l[i]
        else:
            i = i + 1
        t = len(l)
    return l

def calculate5(l : list):
    operators = getOperatorList(5)
    i = 1
    t = len(l) - 1
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '$'):
                    l[i] = getMax(l[i-1] , l[i+1])
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '&'):
                    l[i] = getMin(l[i-1] , l[i+1])
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '@'):
                    l[i] = (l[i-1] + l[i+1])/2
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
        else:
            i = i + 1
        t = len(l) - 1
    return l

def calculate4(l : list):
    operators = getOperatorList(4)
    i = 1
    t = len(l) - 1
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '%'):
                    l[i] = l[i-1] % l[i+1]
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
        else:
            i = i + 1
        t = len(l) - 1
    return l

def calculate3(l : list):
    operators = getOperatorList(3)
    i = 1
    t = len(l) - 1
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '^'):
                    try :
                        l[i] =  math.pow(l[i-1] , l[i+1])
                    except ValueError:
                        raise noComplexFromPower
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
        else:
            i = i + 1
        t = len(l) - 1
    return l

def calculate2(l : list):
    operators = getOperatorList(2)
    i = 1
    t = len(l) - 1
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '/'):
                    l[i] =  l[i-1] / l[i+1]
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '*'):
                    l[i] =  l[i-1] * l[i+1]
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
        else:
            i = i + 1
        t = len(l) - 1
    return l

def calculate1(l : list):
    operators = getOperatorList(1)
    i = 1
    t = len(l) - 1
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '+'):
                    l[i] =  l[i-1] + l[i+1]
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '-' and l[i+1] == '-'):
                    l[i] =  '+'
                    del l[i+1]
                    break
                if (l[i] == '-'):
                    l[i] =  l[i-1] - l[i+1]
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
        else:
            i = i + 1
        t = len(l) - 1
    return l

def calculateWithparenthesis(l : list):
    tempList = []
    i = 0
    t = len(l)
    while i < t:
        if l[i] == ')':
            del l[i]
            i = i - 1
            while (not l[i] == '('):
                tempList.append(l[i])
                del l[i]
                i = i - 1
            tempList.reverse()
            tempList = strToFloat(tempList)
            l[i] = calculation(tempList)
            tempList = []
        else:
            i = i + 1
        t = len(l)
    l = strToFloat(l)
    l = calculation(l)
    return l



