from Consts import *

def isNum(num : str):
    try:
        float(num)
        return True
    except ValueError:
        return False

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
def minusIntoTheNumber(l : list):
    copy =  NoSpaces(l)
    t = len(copy)
    i = 0
    while i<t:
        if i > t-3:
            break
        elif (copy[i] in norightOperators and copy[i+1] == "-" and isNum(copy[i+2])):
            copy[i + 2] = "-" + copy[i+2]
            del copy[i+1]
            t = len(copy)
        else:
            i+=1
    if (copy[0] == '-' and isNum(copy[1])):
        copy[1] = '-' + copy[1]
        del copy[0]
        if (copy[0][0] == '-' and copy[0][1] == '-'):
            copy[0] = copy[0][2]
    return copy


def strToFloat(l : list):
    temp = []
    for i in range(len(l)):
        if (isNum(l[i])):
            temp.append(float(l[i]))
        else:
            temp.append(l[i])
    return temp

