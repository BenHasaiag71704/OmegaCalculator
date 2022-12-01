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

#both of the above
def AllowedAndNoDigSpaceValid(l: list):
    return onlyAllowdCharsValidation(l) and noDigSpacDigValidation(l)

# no - *space* num
def noMinusSpaceDig(l : list):
    for i in range(len(l) - 1):
        if l[i] == ' ':
            if isNum(l[i - 1]) and isNum(l[i + 1]):
                return False
            elif l[i - 1] == '-' and isNum(l[i + 1]):
                if i == 1:
                    return False
                else:
                    if l[i - 2] == ' ':
                        if l[i - 3] in regularOperator or \
                                l[i - 3] in unregularOperator or \
                                l[i - 3] == '(':
                            return False
                    elif l[i - 2] in regularOperator or \
                            l[i - 2] in unregularOperator or \
                            l[i - 2] == '(':
                        return False
    return True
