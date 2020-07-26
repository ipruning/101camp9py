# -*- coding: utf-8 -*-

'''更多文件

'''

from sys import argv ; script, in_file, out_file = argv ; open(out_file, 'w').write(open(in_file).read()) # 一行代码解决

'''
from sys import argv
from os.path import exists

script, in_file, out_file = argv

print(f"Copying from {in_file} to {out_file}")

in_file_data = open(in_file).read()

print(f"The input file is {len(in_file_data)} bytes long")
print(f"Does the output file exist? {exists(out_file)}")
input("Ready, hit RETURN to continue, CTRL-C to abort.")

open(out_file, 'w').write(in_file_data)
'''

'''
out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()
'''
