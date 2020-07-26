# -*- coding: utf-8 -*-
'''提示和传递
https://docs.python.org/zh-cn/3.8/library/sys.html?highlight=argv#sys.argv
argv 和 input() 之间的区别是什么？ 区别取决于用户在哪被要求输入，如果是在命令行，就用 argv。如果你想让它们在程序已经运行的情况下用键盘输入，那就用 input() 。
'''

from sys import argv

print(argv)  #argv 是一个列表

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)