# -*- coding: utf-8 -*-
'''字典，可爱的字典
列表是元素的有序排列。而字典是把一些元素（称为“键”，keys）和另一些元素（称为“值”，values）匹配起来。
我能用字典做什么？ 当你需要用一个东西去查另一个东西的时候。其实，你可以把字典称为“查询表”（look up tables）。
我能用列表做什么？ 可以用于任何有序排列的东西，同时你只需要用数字索引来查找它们。
'''


# 新建字典

states = {
    'Oregon': 'OR',
    "Florida": 'FL',
    'California': 'CA',
    "New York": 'NY',
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
    'NY': 'New York',
    'OR': 'Portland',
}


# 打印字典

print('-' * 10)
print("NY States has: ", cities['NY'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])

print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])  # 组合运用

# 打印所有字典

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

# safely get a abbreviation by state that might not be there

print('-' * 10)
if not states.get('Texas'):
    print("Sorry, no Texas.")

# get a city with a default value

city = cities.get(
    'TX', 'Dose Note Exist'
)  # dict.get(key, default=None) key 是要查找的，default 指的是如果该 key 不存在，返回？
print(f"The city for the state 'TX' is: {city}")
