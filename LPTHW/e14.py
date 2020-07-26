# -*- coding: utf-8 -*-
'''提示和传递

'''

from sys import argv

script, user_name = argv

prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")

print("What kind of computer do you have?")
computer = input(prompt)
print(f"You have a {computer} computer.")