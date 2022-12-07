from Validator import *
from Equation import *
from Fixer import *
from Consts import *



try:
    string = input("enter your Equation here : ")
    e = Equation(string)
    print(e.Equationlist)
    print(e.answer)
except KeyboardInterrupt:
    print([])
