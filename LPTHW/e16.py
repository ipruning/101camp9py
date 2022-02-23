# -*- coding: utf-8 -*-
'''读写文件

如果只输入 open(filename) 是不是就用 'r'（读）模式打开？ 是的，那是 open() 函数的默认值。

'''

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C.")
print("If you do wangt that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')  # 用 Write 模式打开文件

print("Truncating the file. Goodbye!")
target.truncate()  # 清空文件

print("Now I'm going to ask you for three lines.")

line1 = input("line1 = ")
line2 = input("line2 = ")
line3 = input("line3 = ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
print("And finally, we close it.")
target.close()

txt = open(filename)  # 创建文件对象
print(f"Here's your file {filename}:")
print(txt.read())
