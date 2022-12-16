from ProjectFolder.Equation import Equation

import pytest

def testSyntaxError():
    e = Equation("3&&3")
    assert e.answer == None

    e = Equation("3^*2")
    assert e.answer == None

    e = Equation("3~*2")
    assert e.answer == None

    e = Equation("!3")
    assert e.answer == None

    e = Equation("3+(5-1))")
    assert e.answer == None

def testWhiteAndJibrish():
    e = Equation("[]")
    assert e.answer == None

    e = Equation("[ \t  \t    \t]")
    assert e.answer == None

    e = Equation("great success")
    assert e.answer == None

def testBasic():
    e = Equation("--3")
    assert e.answer == 3

    e = Equation("5^2")
    assert e.answer == 25

    e = Equation("(1+2+3+4+5+6)#")
    assert e.answer == 3

    e = Equation("3^3!")
    assert e.answer == 729

    e = Equation("3!!")
    assert e.answer == 720

    e = Equation("3*4$13")
    assert e.answer == 39

    e = Equation("(3*4)$13")
    assert e.answer == 13

    e = Equation("3@5@9@12@15")
    assert e.answer == 12.125

    e = Equation("2.5^2.5")
    assert e.answer == 9.882117688026186

    e = Equation("1+2*3^4.1#")
    assert e.answer == 487.0

    e = Equation("(5&3)@(8$3)")
    assert e.answer == 5.5

    e = Equation("(5/2)/2/2")
    assert e.answer == 0.625

    e = Equation("--10%13 + 5%2 + -7%5")
    assert e.answer == 14

    e = Equation("(5*8*2)^0")
    assert e.answer == 1

    e = Equation("(1.1*1.2)#!")
    assert e.answer == 720

def test_my_test():
    e = Equation("(122+33*(4^3!$(9-8@33)))&(9*21!-93218#)")
    assert e.answer == 135290.0

    e = Equation("((   (5.2)^2@4)# + ~   1.5+3!/0.2   )#^0.5   *5%   3")
    assert e.answer == 8

    e = Equation("(3^(3$     5 - 7*6 + 5.3    912# + 4! -4) +   (~   5   *(--2))%9 + 1)^0.5")
    assert e.answer == 6

    e = Equation("(   (-5    @(-7+(  4$(5   &4 + 5   %3)^   4)))#-    7)   ! % 3.5*5")
    assert e.answer == 5

    e = Equation("((5!^5%3)#)^((5!^5%3)# @ 1 + ~8/4) * (1/27)")
    assert e.answer == 27

    e = Equation("((  (3-  -2+~5)!/0. 0 4 * (5 & 10*3$4  + 1/8)# % 7)#/2)@10")
    assert e.answer == 8

    e = Equation("(5!@4%32^2/90*1.5-5+10)*3 + (5-( 2 ^ 32 % 4 @ 5!)#)")
    assert e.answer == 7

    e = Equation("(((((((--4)^(--2))#!#^2)*0.3)#/4.5)^6)%8)@100 * 10 / 5 + 2")
    assert e.answer == 102

    e = Equation("((150%52   %3)@49^0.5) $ (  1/(  1+(1/(   1+(  1/(1+  (1/(1+1) )) ) ) ) ) )# * 3 / 2.5")
    assert e.answer == 15.6

    e = Equation("(3/  2 ) +( 6  *2)-5! + 3^5 -   2  ^6 * 3  .5 - (16  ^0.5)^  0.5 - 9 %2 ^10")
    assert e.answer == -90.5

    e = Equation("(((3$4$5$6$7 + 3@4@5@6@7 + 3&4&5&6&7 - 1/16)^0.5 + 1.678)#%23)!--5*2")
    assert e.answer == 16

    e = Equation("((( ( ( - -2) ^(- -2 ))*( (3 --3+- -3) ^( 0.5))) !#^ (1/ 3)  )! !) %(4  7)^2")
    assert e.answer == 225

    e = Equation("1/((--5*--3^--2+--4!%--13--4*--2---3----7)#) + 4@5$6 + 4@(5$6)")
    assert e.answer == 11.071428571428571

    e = Equation("6 -(1/((1+5^0.5)/2) + 1/(((1+5^0.5)/2)^2) + (20+((20+(20+(20^0.5))^0.5)^0.5))^0.5) - 0.0005309903763039969")
    assert e.answer == 0

    e = Equation("86028# + 125*31 - 4^((3.7^2)# - 15) - 5^(-~--3) - 6! - 1582@924")
    assert e.answer == 777

    e = Equation("((   (5.2)^2@4)# + ~   1.5+3!/0.2   )#^0.5   *5%   3")
    assert e.answer == 8