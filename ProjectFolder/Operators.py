class Operators(object):
    OperatorDict = {
        "+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "%": 5, "$": 5, "@": 5, "~": 6, "!": 6,
    }
    def __int__(self):
        self.OperatorDict

    def __str__(self):
        print(self.OperatorDict)
