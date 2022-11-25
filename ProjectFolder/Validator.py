class Validator(object):
    def FirstValidation(l: list):
        OperatorList = ["+", "-", "*", "/", "^", "%", "$", "@", "~", "!", " ", "\t", "(", ")"]
        for i in l:
            if not i.isdecimal():
                if not OperatorList.count(i) == 1:
                    return False
        return True

