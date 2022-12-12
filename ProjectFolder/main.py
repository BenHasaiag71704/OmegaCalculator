from Validator import *
from Equation import *
from Fixer import *
from Consts import *







try:
    string = input("enter your Equation here : ")
except KeyboardInterrupt:
    print([])
finally:
    e = Equation(string)
    print(e.answer)
