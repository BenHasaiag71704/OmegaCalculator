from Consts import *


def swapAllTabs(l: list):
    for i in range(len(l)):
        if (l[i] == "\t"):
            l[i] = " "
    return l


def NoDoubleSpaces(l: list):
    tempList = []
    for i in range(len(l)):
        if (not l[i] == " "):
            tempList.append(l[i])
    return tempList


def charsIntoNumbers(l: list):
    i = 0
    num = 0
    decimalPlace = 10
    tempList = []
    flag = True
    flagPoint = False
    while i < len(l):
        flagPoint = False
        flag = True
        num = 0
        decimalPlace = 10
        if (OperatorList.count(l[i]) == 1):
            tempList.append(l[i])
        if l[i].isdigit():
            while (l[i].isdigit() and i < len(l) - 1):
                num = num * 10 + int(l[i])
                i = i + 1
            if (l[i] == "." and i < len(l) - 1):
                i = i + 1
                while (l[i].isdigit() and i < len(l) - 1):
                    num = num + (int(l[i])/decimalPlace)
                    decimalPlace = decimalPlace * 10
                    i = i + 1
                    flagPoint = True
            if (i == len(l) - 1 and not flagPoint and l[i-1]== "."):
                tempList.append(num + int(l[i])/decimalPlace)
                return tempList
            if (i == len(l) - 1 and not flagPoint):
                if (l[i] == "."):
                    tempList.append(num)
                else:
                    tempList.append(num*10 + int(l[i]))
                return tempList
            if (i == len(l) - 1 and flagPoint):
                tempList.append(num + int(l[i])/decimalPlace)
                return tempList
            else:
                flag = False
                tempList.append(num)
            num = 0
        if (flag and len(l) - 1):
            i = i + 1
    return tempList

