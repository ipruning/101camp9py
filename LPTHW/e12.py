age = input("How old are you?")
print(f"You are {age} old.")
print("How old are you?", input())
# Why can’t I do print("How old are you?" , input())?
# You can, but then the result of calling input() is never saved to a variable, antd it’ll work in a strange way.
# Try this, and then try to print out what you type. See if you can debug why this isn’t working.
