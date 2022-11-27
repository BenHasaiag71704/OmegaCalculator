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
    # i to store the index , num to store the num to add , decimalplace to calculator correcly the decimal numbers
    i = 0
    num = 0
    decimalPlace = 10
    tempList = []
    # flag - was a number added? (means we did the i++ so no need again)
    flag = True
    # were we adding decimal number?
    flagPoint = False
    while i < len(l):
        flagPoint = False
        flag = True
        num = 0
        decimalPlace = 10
        # not a number , add the operator
        if (OperatorList.count(l[i]) == 1):
            tempList.append(l[i])
        # if its a number
        if l[i].isdigit():
        #as long as we see digits
            while (l[i].isdigit() and i < len(l) - 1):
                # sums the number
                num = num * 10 + int(l[i])
                i = i + 1
            # we also need to take care of decimal case!
            if (l[i] == "." and i < len(l) - 1):
                i = i + 1
                # sum the decimal
                while (l[i].isdigit() and i < len(l) - 1):
                    num = num + (int(l[i])/decimalPlace)
                    decimalPlace = decimalPlace * 10
                    i = i + 1
                    flagPoint = True
            # if we are at the end of the list , and there is  nothing in number (0.something) , with this 0.1 will return 1
            if (i == len(l) - 1 and not flagPoint and l[i-1]== "."):
                tempList.append(num + int(l[i])/decimalPlace)
                return tempList
            # in case where . was the last point
            if (i == len(l) - 1 and not flagPoint):
                if (l[i] == "."):
                    tempList.append(num)
                else:
                    tempList.append(num*10 + int(l[i]))
                return tempList
            #  in case we ended the loop at decimal place
            if (i == len(l) - 1 and flagPoint):
                tempList.append(num + int(l[i])/decimalPlace)
                return tempList
            # in case of entering int number
            else:
                flag = False
                tempList.append(num)
            num = 0
        if (flag and len(l) - 1):
            i = i + 1
    return tempList

