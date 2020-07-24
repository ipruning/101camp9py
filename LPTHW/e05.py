# -*- coding: utf-8 -*-
'''More Variables and Printing

print 字符串之前用 f 外加 {}

'''

my_name = 'Zed A. Shaw'
my_age = 35
my_height = 74
my_weight = 180
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

my_height_cm = 2.54 * my_height
my_weight_kg = round(0.45 * my_weight)  # 函数"round()"的作用是给数值四舍五入成整数。
