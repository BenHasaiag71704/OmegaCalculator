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
    try:
        int(s)
    except:
        raise numberToBigToSum
    return int(s)

def factorial(f : float):
    if (f == 0):
        return 1
    if (f < 0):
        raise NegetiveFactorialException
    sum = 1
    if (float(f).is_integer()):
        if (f > 170):
            raise numberToBig
        while (f > 1):
            sum = sum * f
            f = f - 1
    else:
        raise floatFactorial
    return sum

def sumOfDig(f : float):
    temp = removeDecimal(f)
    sum = 0
    flag = False
    if (temp < 0):
        flag = True
        temp = - temp
    while (temp > 0):
        sum = sum + temp % 10
        temp = int(temp/10)
    if (flag):
        return -sum
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
                    l[i - 1] = sumOfDig( l[i - 1])
                    del l[i]
                    break
        elif l[i] in leftOperators and l[i] in operators:
            if l[i] == '~':
                if l[i+1] != '-':
                    l[i + 1] =  -(l[i + 1])
                    del l[i]
                else:
                    del l[i]
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
                    l = fixExtraMinus(l,i)
                    l[i] = getMax(l[i-1] , l[i+1])
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '&'):
                    l = fixExtraMinus(l,i)
                    l[i] = getMin(l[i-1] , l[i+1])
                    del l[i-1]
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '@'):
                    l = fixExtraMinus(l,i)
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
                try :
                    if (l[i] == '%'):
                        l = fixExtraMinus(l, i)
                        l[i] = l[i-1] % l[i+1]
                        del l[i-1]
                    #not i+1 bcz we just deleted number!
                        del l[i]
                        break
                except ZeroDivisionError:
                    raise zeroModulo
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
                    l = fixExtraMinus(l,i)
                    try :
                        l[i] =  math.pow(l[i-1] , l[i+1])
                    except ValueError:
                        raise noComplexFromPower
                    except OverflowError:
                        raise numberToBig
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
                    l = fixExtraMinus(l,i)
                    try :
                        l[i] =  l[i-1] / l[i+1]
                        del l[i-1]
                    except ZeroDivisionError:
                        raise zeroDevission
                    #not i+1 bcz we just deleted number!
                    del l[i]
                    break
                if (l[i] == '*'):
                    l = fixExtraMinus(l,i)
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
    n = len(l)
    if (len(l) >=2):
        if l[0] == '-':
            del l[0]
            l[0] = -l[0]
    while i < t:
        if (l[i] in operators and l[i] in regularOperator):
            while True:
                if (l[i] == '+'):
                    l = fixExtraMinus(l,i)
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
    if len(l) == 2:
        l[1] = -l[1]
        del l[0]
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


def fixExtraMinus(l:list , i:int):
    n = len(l)
    if (i < n-2):
        if (l[i] in regularOperator and l[i+1] == '-'):
            del l[i+1]
            l[i+1] = -l[i+1]
    return l