from Validator import *
from Fixer import *
from Calculations import *
from allExceptions import *



# delete all space doubles
# check all chars are allowed + check dig space dig


class Equation(object):
    def __init__(self, MyInput):
        Equationlist = list(MyInput)
        print("original Equation :" , Equationlist)
        if (OnlyWhiteSpaces(Equationlist)):
            Equationlist = []
            self.answer = None
        else:
            Equationlist.insert(0, '(')
            Equationlist.append(')')
            flag = AllowedAndNoDigSpaceValid(Equationlist)
            Equationlist = NoSpaces(Equationlist)

            Equationlist = noDoubleSpaces(Equationlist)
            Equationlist = convertTofloats(Equationlist)
            Equationlist = fixDecimalPoint(Equationlist)

            #print("list without doubleSpaces , with decimals" , Equationlist)

            #flag5 = noNegetivrFactorialAtTheBegine(Equationlist)
            #and flag5

            Equationlist = removeMultipuleMinus(Equationlist)
            #print("list without Multipule Minus" ,Equationlist)


            Equationlist = minusIntoTheNumber(Equationlist)
            #print(Equationlist)

            ###############
            #Equationlist = firstMinusesIntoNumber(Equationlist)

            ##########

            #print(Equationlist)

            #print("list with Minus inside the numbers" ,Equationlist)

            #can be added if needed -_3 valid
            #flag2 = noMinusSpaceDig(Equationlist)


            #would be here when -_3 valid
            #Equationlist = NoSpaces(Equationlist)
            #print(Equationlist)

            flag3 = ParenthesisValidation(Equationlist)
            flag4 = allOperatorValidation(Equationlist)

            #flag5 = noNegetivehastagclal(Equationlist)
            #and flag5

            #print(Equationlist)

            flag6 = doesntStartWithRegular(Equationlist)
            #and flag2 for -_2 valid
            if (flag  and flag3 and flag4 and flag6):
                Equationlist = strToFloat(Equationlist)
                #print(Equationlist)
                self.Equationlist = Equationlist
                try:
                    self.answer = calculateWithparenthesis(Equationlist)
                except NegetiveFactorialException:
                    print("you cant factorial negetive number")
                    self.answer = None
                except floatFactorial:
                    print("you cant factorial float number")
                    self.answer = None
                except noComplexFromPower:
                    print("you cant power negetive^fraction")
                    self.answer = None
                except numberToBig:
                    print("the result was to big to store in a number , consider the answer as infinity")
                    self.answer = None
                except numberToBigToSum:
                    print("can sum numbers when the numbers are up to 10^16")
                    self.answer = None
                except zeroDevission:
                    print("cant devide by 0!")
                    self.answer = None
                except zeroModulo:
                    print("cant find modulo 0!")
                    self.answer = None
            else:
                self.Equationlist = []
                self.answer = None