from Validator import *
from Fixer import *
class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        print(Equationlist)
        if (AbsoluteValid(Equationlist)):
            Equationlist = NoDoubleSpaces(Equationlist)
            print(Equationlist)
            Equationlist = charsIntoNumbers(Equationlist)
            self.Equationlist = Equationlist
        else:
            print("there is an error in the input")
            self.Equationlist = []