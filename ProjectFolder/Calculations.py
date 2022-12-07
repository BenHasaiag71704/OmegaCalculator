from Consts import *

def getOperatorList(f : int):
    temp = []
    for k, v in OperatorDict.items():
        if v == f:
            temp.append(k)
    return temp

def removeDecimal(f: float) -> int:
    s = str(f)
    s = s.replace('.', '')
    return int(s)




def factorial(f : float):
    if (f == 0):
        return 0
    if (f < 0):
        print("cant factorial float")
        return -1
    sum = 1
    if (float(f).is_integer()):
        while (f > 1):
            sum = sum * f
            f = f - 1
    else:
        print("cant factorial float")
        return -1
    return sum

def sumOfDig(f : float):
    temp = removeDecimal(f)
    sum = 0
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


    return l


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

temp = [5 , '$' , 7 , '$' , 9]
#temp = [3 , '!' , '!']
temp = calculate5(temp)
print(temp)


print(getOperatorList(5))

i = 6

