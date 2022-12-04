from Validator import *
from Fixer import *

# delete all space doubles
# check all chars are allowed + check dig space dig


class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        print("original list :" , Equationlist)

        flag = AllowedAndNoDigSpaceValid(Equationlist)

        Equationlist = noDoubleSpaces(Equationlist)
        Equationlist = convertTofloats(Equationlist)
        Equationlist = fixDecimalPoint(Equationlist)
        print("list without doubleSpaces , with decimals" , Equationlist)

        Equationlist = removeMultipuleMinus(Equationlist)
        print("list without Multipule Minus" ,Equationlist)

        Equationlist = minusIntoTheNumber(Equationlist)
        print("list with Minus inside the numbers" ,Equationlist)

        flag2 = noMinusSpaceDig(Equationlist)

        Equationlist = NoSpaces(Equationlist)
        print(Equationlist)

        flag3 = ParenthesisValidation(Equationlist)
        flag4 = allOperatorValidation(Equationlist)

        if (flag and flag2 and flag3 and flag4):
            self.Equationlist = Equationlist
        else:
            self.Equationlist = []