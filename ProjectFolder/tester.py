from ProjectFolder.Equation import Equation

import pytest

def test_my_test():
    e = Equation("(122+33*(4^3!$(9-8@33)))&(9*21!-93218#)")
    assert e.answer == 135290.0

    e = Equation("great success")
    assert e.answer == None

    #e = Equation("1/((--5*--3^--2+--4!%--13--4*--2---3----7)#) + 4@5$6 + 4@(5$6)")
    #assert e.answer == 11.071428571428571