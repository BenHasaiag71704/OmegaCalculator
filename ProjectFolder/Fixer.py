def swapAllTabs(l:list):
    for i in range(len(l)):
        if (l[i] == "\t"):
            l[i]= " "
    return l

def NoDoubleSpaces(l:list):
    tempList = []
    for i in range(len(l)):
        if (not l[i] == " "):
            tempList.append(l[i])
    return tempList