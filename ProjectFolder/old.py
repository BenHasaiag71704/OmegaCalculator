
# old unused funcs


# #the old fucntion
# from Consts import *
# def charsIntoNumbers(l: list):
#     # i to store the index , num to store the num to add , decimalplace to calculator correcly the decimal numbers
#     i = 0
#     num = 0
#     decimalPlace = 10
#     tempList = []
#     # flag - was a number added? (means we did the i++ so no need again)
#     flag = True
#     # were we adding decimal number?
#     flagPoint = False
#     while i < len(l):
#         flagPoint = False
#         flag = True
#         num = 0
#         decimalPlace = 10
#         # not a number , add the operator
#         if (OperatorList.count(l[i]) == 1):
#             tempList.append(l[i])
#         # if its a number
#         if l[i].isdigit() or l[i] == ".":
#         #as long as we see digits
#             while (l[i].isdigit() and i < len(l) - 1):
#                 # sums the number
#                 num = num * 10 + int(l[i])
#                 i = i + 1
#             # we also need to take care of decimal case!
#             if (l[i] == "." and i < len(l) - 1):
#                 i = i + 1
#                 # sum the decimal
#                 while (l[i].isdigit() and i < len(l) - 1):
#                     num = num + (int(l[i])/decimalPlace)
#                     decimalPlace = decimalPlace * 10
#                     i = i + 1
#                     flagPoint = True
#             # if we are at the end of the list , and there is  nothing in number (0.something) , with this 0.1 will return 1
#             if (i == len(l) - 1 and not flagPoint and l[i-1]== "."):
#                 tempList.append(num + int(l[i])/decimalPlace)
#                 return tempList
#             # in case where . was the last point
#             if (i == len(l) - 1 and not flagPoint):
#                 if (l[i] == "."):
#                     tempList.append(num)
#                 else:
#                     if (not l[i].isdigit()):
#                         tempList.append(num)
#                         tempList.append(l[i])
#                     else:
#                         tempList.append(num*10 + int(l[i]))
#                 return tempList
#             #  in case we ended the loop at decimal place
#             if (i == len(l) - 1 and flagPoint):
#                 if (not l[i].isdigit()):
#                     tempList.append(num)
#                     tempList.append(l[i])
#                 else :
#                     tempList.append(num + int(l[i])/decimalPlace)
#                 return tempList
#             # in case of entering int number
#             else:
#                 flag = False
#                 tempList.append(num)
#             num = 0
#         if (flag and len(l) - 1):
#             i = i + 1
#     return tempList
#
# #not work
# def charsIntoNumbersRecusiveBroken(l : list) ->None:
#     flag = True
#     i = 0
#     while i <len(l) and flag:
#         if (l[i] == '.'):
#             while (l[i+1].isdigit()):
#                 l[i]+=l[i+1]
#                 del l[i+1]
#                 flag = False
#                 break
#             while (l[i-1].isdigit()):
#                 l[i]=l[i-1]+l[i]
#                 del l[i-1]
#                 flag = False
#                 break
#         i+=1
#     if ('.' in l):
#         charsIntoNumbers(l)
#
#
# def noNegetivrFactorialAtTheBegine(l:list):
#     temp = NoSpaces(l)
#     i = 0
#     flag = False
#     while (temp[i] == '-' and i < len(temp)):
#         i=i+1
#         flag = True
#     if (flag):
#         if (i+1 < len(temp)):
#             if (isNum(temp[i]) and temp[i+1] == '!' ):
#                 print("cant factorial a number")
#                 return False
#     return True
#
# def minusIntoTheNumberOLD(l : list):
#     copy =  NoSpaces(l)
#     t = len(copy)
#     i = 0
#     while i<t:
#         if i > t-3:
#             break
#         elif (copy[i] in norightOperators and copy[i+1] == "-" and isNum(copy[i+2])):
#             copy[i + 2] = "-" + copy[i+2]
#             del copy[i+1]
#             t = len(copy)
#         else:
#             i+=1
#     if (copy[0] == '-' and isNum(copy[1])):
#         copy[1] = '-' + copy[1]
#         del copy[0]
#         if (copy[0][0] == '-' and copy[0][1] == '-'):
#             copy[0] = copy[0][2]
#     return copy
#
