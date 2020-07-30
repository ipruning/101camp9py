# -*- coding: utf-8 -*-
'''操作列表
mystuff.append('hello') 的本质是 append(mystuff, 'hello')
s.pop([i]) 提取在 i 位置上的项，并将其从序列中移除；可选参数 i 默认为 -1，因此在默认情况下会移除并返回最后一项。
split() method splits a string into a list.
'''

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ')
more_stuff = [
    "Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"
]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print('#'.join(stuff[3:5]))  # 抽取 3-4 的切片
