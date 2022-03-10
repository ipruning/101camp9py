# -*- coding: utf-8 -*-
'''字符串，字节和字符编码
ord('Z')
chr(90)
'''

import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    if line := language_file.readline():
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors) # 递归


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


language = open("e23.txt", encoding="utf-8")

main(language, encoding, error)
