# -*- coding: utf-8 -*-
'''循环和列表
'''


the_count = [1, 2, 3, 4,5 ] # list
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3 , 'quarters']

for number in the_count:
    print(f"This is count {number}")

for fruit in fruits: # 这种循环的写法蛮意外，Python 中 for 会遍历任何序列，List Tuple 迭代器
    print(f"A fruit of type: {fruit}")

for i in change:
    print(f"I got {i}")

elements = [] # 新建 List

for i in range(6):
    print(f"Adding {i} to the list.")
    elements.append(i)

for i in elements:
    print(f"Element was: {i}")
