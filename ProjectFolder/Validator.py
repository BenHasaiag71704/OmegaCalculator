from Consts import *
from Fixer import *

def isAnumber(String : str):
    pass


def onlyAllowdCharsValidation(l: list):
    for i in l:
        if not i.isdecimal():
            if not AllowedList.count(i) == 1:
                return False
    return True

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

#no double spaces + all the numbers already turned into floats
