from Validator import *
from Fixer import *

# delete all space doubles
# check all chars are allowed + check dig space dig


class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        print(Equationlist)

        flag = AllowedAndNoDigSpaceValid(Equationlist)

        Equationlist = noDoubleSpaces(Equationlist)
        Equationlist = convert_to_floats(Equationlist)
        Equationlist = fixDecimalPoint(Equationlist)


        print(Equationlist)
        #check - 3

        Equationlist = NoSpaces(Equationlist)

        #check same ( ) number
        #flag2 = check operators

        if (flag):
            self.Equationlist = Equationlist
        else:
            print("there is an error in the input")
            self.Equationlist = []