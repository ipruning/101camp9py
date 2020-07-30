# -*- coding: utf-8 -*-
'''模块、类和对象
你可以把模块想象成一个可以储存 Python 代码并且可以用 . 运算符获取它的特定字典。
Python 还有一种类似功能的结构叫做类（class）。
类是一种整合一组函数和数据的方式，它将函数和数据放在一个容器内以便你能通过 . 运算符进行访问。
'''

import e40a

e40a.apple()
print(e40a.tangerine)
'''对比字典
e40a['apple'] # get apple from dict
e40a.apple() # get apple from the module
e40a.tangerine # same thing, it's just a variable
'''
'''模式总结
有一个 key <=> value 容器
通过 key 名称获取 value 在 dict 中，key 是 string 语法是 [key] 在模块中，key 是一个识别符，语法是 .key
'''
