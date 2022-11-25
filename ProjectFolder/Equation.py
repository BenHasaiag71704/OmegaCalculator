from Validator import *


class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        if (Validator.FirstValidation(Equationlist)):
            self.Equationlist = Equationlist
        else:
            print("there is an error in the input")
            self.Equationlist = []