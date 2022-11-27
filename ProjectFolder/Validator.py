from Consts import *

def FirstValidation(l: list):
    OperatorList
    for i in l:
        if not i.isdecimal():
            if not AllowedList.count(i) == 1:
                return False
    return True

def SecondValidation(l: list):
    tempBack = ''
    i = 0
    while i < len(l):
        if (l[i] == " " and i > 0):
            tempBack = l[i - 1]
            while (l[i] == " " and i < len(l) - 1):
                i = i + 1
        if (tempBack.isdigit() and l[i].isdigit()):
            return False
        if (OperatorList.count(l[i]) == 1):
            tempBack = ''
        i = i + 1
    return True

def AbsoluteValid(l: list):
    return FirstValidation(l) and SecondValidation(l)

