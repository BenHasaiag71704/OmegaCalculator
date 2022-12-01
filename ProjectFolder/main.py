from Validator import *
from Equation import *
from Fixer import *

def charsIntoNumbers(l : list) ->None:
    flag = True
    i = 0
    while i < len(l) and flag:
        if (l[i] == '.'):
            while (l[i+1].isdigit()):
                l[i]+=l[i+1]
                del l[i+1]
                flag = False
                break
            while (l[i-1].isdigit()):
                l[i]=l[i-1]+l[i]
                del l[i-1]
                flag = False
                break
        i+=1
    if ('.' in l):
        charsIntoNumbers(l)

def convert_to_floats(equation: list) -> list:
    new_equation = []
    index = 0
    length = len(equation)
    current_number = ''
    while index < length:
        if equation[index].isdigit():
            current_number += equation[index]
        elif equation[index] == '.':
            current_number += equation[index]
        else:
            if current_number != '':
                new_equation.append(current_number)
                current_number = ''
            new_equation.append(equation[index])
        index += 1

    if current_number != '':
        new_equation.append(current_number)
    return new_equation



string = input("enter your Equation here : ")

e = Equation(string)

print(e.Equationlist)
