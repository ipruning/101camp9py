# -*- coding: utf-8 -*-
'''问问题

'''

print("How old are you?", end=' ') # 每一个打印行末尾放一个 end=' ' ，是为了告诉 print 不要另起一行。
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weight?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")
