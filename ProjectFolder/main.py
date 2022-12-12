from Validator import *
from Equation import *
from Fixer import *
from Consts import *





string = None

while string == None:
    try:
        string = input("enter your Equation here : ")
    except KeyboardInterrupt:
        print([])
    except UnicodeDecodeError:
        print([])
    except EOFError:
        print([])
        string = 'd'
        break

e = Equation(string)
print(e.answer)
