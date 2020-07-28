# -*- coding: utf-8 -*-
'''函数和文件
readline() 扫描整个文件，当遇到 \n 字符，会停止扫描。
'''

from sys import argv

script, input_file = argv


def print_all(f):
    print(f.read())


def rewind(f):
    f.seek(0)  # 这个代码把文件移动到 0 字节


def print_a_line(line_count, f):
    print(line_count, f.readline())


current_files = open(input_file)

print("First let's print the whole file:\n")

print_all(current_files)

print("Now let's rewind, kind of like a tape.")

rewind(current_files)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_files)

current_line += current_line
print_a_line(current_line, current_files)

current_line += current_line
print_a_line(current_line, current_files)
