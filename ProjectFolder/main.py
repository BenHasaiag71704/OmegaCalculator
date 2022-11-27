from Validator import *
from Equation import *


string = input("enter your Equation here : ")

e = Equation(string)

def swapAllTabs(l:list):
    for i in range(len(l)):
        if (l[i] == "\t"):
            l[i]= " "
    return l








