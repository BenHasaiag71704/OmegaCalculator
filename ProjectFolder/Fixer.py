from Consts import *


#check if str is a number
def isNum(num : str):
    try:
        float(num)
        return True
    except ValueError:
        return False

#convert list into string
def listToString(l : list):
    str1 = ""
    return (str1.join(l))

#remove all places where there is more then one space and replace it with single space
def noDoubleSpaces(l : list):
    str1 = listToString(l)
    while '  ' in str1 or '\t' in str1 or '\n' in str1:
        str1 = str1.replace('  ',' ')
        str1 = str1.replace('\t',' ')
        str1 = str1.replace('\n',' ')
    return list(str1)

# remove all spaces
def NoSpaces(l: list):
    tempList = []
    for i in range(len(l)):
        if (not l[i] == " "):
            tempList.append(l[i])
    return tempList

# fix x. and .x
def fixDecimalPoint(l: list):
    s = ''
    for i in range(len(l)):
        s = l[i]
        if "." == s[-1]:
            s = s[:-1]
        elif "." == s[0]:
            s = '0' + s
        l[i] = s
    return l

# convert to decimal point
def convertTofloats(l: list) -> list:
    new_equation = []
    index = 0
    length = len(l)
    current_number = ''
    while index < length:
        if l[index].isdigit():
            current_number += l[index]
        elif l[index] == '.':
            current_number += l[index]
        else:
            if current_number != '':
                new_equation.append(current_number)
                current_number = ''
            new_equation.append(l[index])
        index += 1

    if current_number != '':
        new_equation.append(current_number)
    return new_equation

# remove all multipule minuses , exa --- to - , or  ---- to --
def removeMultipuleMinus(l : list):
    copy = NoSpaces(l)
    t = len(copy)
    i = 0
    while i < t:
        if (i > t-3):
            break
        if (copy[i] == copy[i+1] and copy[i+1] == copy[i+2] and copy[i]== '-'):
            del copy[i]
            del copy[i+1]
            t = len(copy)
        else:
            i+=1
    return copy

#insert the minus into the number when needed

#if there is a numebr , -- into + , else , -- into nothing
def minusIntoTheNumber(l : list):
    i = 1
    t = len(l)
    while i < t - 1:
        if (l[i] == '-' and l[i+1] == '-'):
            while (True):
                if (l[i-1] in norightOperators and l[i-1] != ')'):
                    del l[i]
                    del l[i]
                    t = len(l)
                    i = i + 1
                    break
                if (isNum(l[i-1]) or l[i-1] == '!' or l[i-1] == ')'):
                    del l[i]
                    l[i] = "+"
                    t = len(l)
                    break
        elif (l[i] == '-' and isNum(l[i+1])) and (l[i-1] in norightOperators and l[i-1] != ')'):
            if float(l[i+1]) > 0:
                del l[i]
                l[i] = "-" + l[i]
                t = len(l)
            else:
                del l[i]
                l[i] = l[i][1:]
                t = len(l)
        # elif (l[i] == '-' and l[i+1] != '-'):
        #     if (l[i-1] in norightOperators and l[i-1] != ')'):
        #         del l[i]
        #         while i < len(l) and not isNum(l[i]):
        #             i = i + 1
        #         if (i != len(l)):
        #             l[i] = "-" + l[i]
        #             i = 0
        #         t = len(l)
        #     i = i + 1
        else:
            i = i + 1
    return l

def firstMinusesIntoNumber(l:list):
    i = 0
    count = 0
    while l[i] == '(':
        i = i + 1
    if (l[i] == '-' and l[i+1] == '-'):
        del l[i]
        del l[i]
    if (l[i] == '-' and l[i+1] != '-'):
        del l[i]
        while not isNum(l[i]):
            i = i + 1
        l[i] = "-" + l[i]

    if (not isNum(l[0])):
        if (l[0] != "~"):
            if (len(l[0]) >= 3):
                temp = l[0][2:]
                l[0] = temp
        else:
            if (len(l[1]) >= 3):
                temp = l[1][2:]
                l[1] = temp
    return l


#convert all numbers in the list from str to floar , means ['1','+','1'] will be [1,'+',1]
def strToFloat(l : list):
    temp = []
    for i in range(len(l)):
        if (isNum(l[i])):
            temp.append(float(l[i]))
        else:
            temp.append(l[i])
    return temp



