# -*- coding: utf-8 -*-
'''While 循环
'''


def print_number_list(max):
    i = 0
    numbers = []

    while i < max:
        print(f"At the top i is {i}")
        numbers.append(i)

        i = i + 1  #累加器
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    print("The numbers:")

    for num in numbers:
        print(num)


print_number_list(int(input()))
