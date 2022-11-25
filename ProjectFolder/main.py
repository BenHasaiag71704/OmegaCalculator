from Validator import *
from Equation import *


string = input("enter your Equation here : ")

e = Equation(string)


# will be space validation
def SecondValidation(l: list):
    return True

t = SecondValidation(e.Equationlist)
print(e.Equationlist)
print(t)


