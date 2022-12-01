from Consts import *


def listToString(l : list):
    str1 = ""
    return (str1.join(l))


def noDoubleSpaces(l : list):
    str1 = listToString(l)
    while '  ' in str1 or '\t' in str1 or '\n' in str1:
        str1 = str1.replace('  ',' ')
        str1 = str1.replace('\t',' ')
        str1 = str1.replace('\n',' ')
    return list(str1)


def NoSpaces(l: list):
    tempList = []
    for i in range(len(l)):
        if (not l[i] == " "):
            tempList.append(l[i])
    return tempList


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


def convertTofloats(equation: list) -> list:
    new_equation = []
    index = 0
    length = len(equation)
    current_number = ''
    while index < length:
        if equation[index].isdigit():
            current_number += equation[index]
        elif equation[index] == '.':
            current_number += equation[index]
        else:
            if current_number != '':
                new_equation.append(current_number)
                current_number = ''
            new_equation.append(equation[index])
        index += 1

    if current_number != '':
        new_equation.append(current_number)
    return new_equation
