# -*- coding: utf-8 -*-
'''阅读文件

txt.read 报错 <built-in method read of _io.TextIOWrapper object at 0x7f803767e210> 原因是
If you don't have the brackets, all you are doing is obtaining the read method and assigning it to a.
Thus, when you print a you see a piece of text describing the method

'''

from sys import argv

script, filename = argv

txt = open(filename) # 创建文件对象

print(f"Here's your file {filename}:")
print(txt.read())
