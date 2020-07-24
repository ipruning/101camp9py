# -*- coding: utf-8 -*-
'''Printing, Printing

'''

formatter = "{} {} {} {}"  # define formatter string
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))  # 套娃

print()
print("那么我还可以试试：")
x = 5
x = x * x
print(formatter.format(formatter.format(1, 2, 3, 4), formatter, 3, x))
