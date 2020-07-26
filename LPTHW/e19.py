# -*- coding: utf-8 -*-

'''函数与变量
传入函数的变量是局部变量
'''

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")


cheese_and_crackers(20, 30)
cheese_and_crackers(10 + 20, 5 + 6)
cheese_and_crackers(input("cheese_count = "), input("boxes_of_crackers = "))