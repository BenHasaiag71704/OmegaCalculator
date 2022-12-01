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
        Equationlist = convertTofloats(Equationlist)
        Equationlist = fixDecimalPoint(Equationlist)


        print(Equationlist)
        flag2 = noMinusSpaceDig(Equationlist)

        Equationlist = NoSpaces(Equationlist)
        print(Equationlist)

        flag3 = ParenthesisValidation(Equationlist)
        #flag2 = check operators

        if (flag and flag2 and flag3):
            self.Equationlist = Equationlist
        else:
            self.Equationlist = []