# -*- coding: utf-8 -*-

'''名称，变量，代码，函数

'''

def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
