from Validator import *
from Fixer import *
from Calculations import *
from allExceptions import *



# delete all space doubles
# check all chars are allowed + check dig space dig


class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        print("original list :" , Equationlist)

        flag = AllowedAndNoDigSpaceValid(Equationlist)
        Equationlist = NoSpaces(Equationlist)

        Equationlist = noDoubleSpaces(Equationlist)
        Equationlist = convertTofloats(Equationlist)
        Equationlist = fixDecimalPoint(Equationlist)
        print("list without doubleSpaces , with decimals" , Equationlist)

        #flag5 = noNegetivrFactorialAtTheBegine(Equationlist)
        #and flag5

        Equationlist = removeMultipuleMinus(Equationlist)
        print("list without Multipule Minus" ,Equationlist)


        Equationlist = minusIntoTheNumber(Equationlist)


        Equationlist = firstMinusesIntoNumber(Equationlist)

        print("list with Minus inside the numbers" ,Equationlist)

        #can be added if needed -_3 valid
        #flag2 = noMinusSpaceDig(Equationlist)


        #would be here when -_3 valid
        #Equationlist = NoSpaces(Equationlist)
        print(Equationlist)

        flag3 = ParenthesisValidation(Equationlist)
        flag4 = allOperatorValidation(Equationlist)

        #flag5 = noNegetivehastagclal(Equationlist)
        #and flag5

        flag6 = doesntStartWithRegular(Equationlist)

        #and flag2 for -_2 valid
        if (flag  and flag3 and flag4 and flag6):
            Equationlist = strToFloat(Equationlist)
            self.Equationlist = Equationlist
            try:
                self.answer = calculateWithparenthesis(Equationlist)
            except NegetiveFactorialException:
                print("you cant factorial negetive number")
                self.answer = 0
            except floatFactorial:
                print("you cant factorial float number")
                self.answer = 0
            except noComplexFromPower:
                print("you cant power negetive^fraction")
                self.answer = 0
            except numberToBig:
                print("the maximing number python can sum is up to 1*10^16")
                self.answer = 0

        else:
            self.Equationlist = []
            self.answer = None